from pathlib import Path
from json import dumps
from typing import Any, overload, TYPE_CHECKING

from ...core.component import Component
from ...core import Empty, JS
from ...internal.constants import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE
from ...rendering.tree import ElementNode

from ..feature import Feature

if TYPE_CHECKING:
    from ...context import Context

HERE = Path(__file__).parent
_EMPTY = object()


class _StateMeta(type):
    _instances = {}

    def __call__(self, name: str, *args: Any, **kwds: Any):
        if name not in self._instances:
            self._instances[name] = super().__call__(name, *args, **kwds)
        return self._instances[name]

    def __iter__(self):
        return iter(self._instances.values())


class State(metaclass=_StateMeta):
    def __init__(self, name: str, default_value=None):
        self.name = name
        self.default_value = default_value
        self.props = {
            "init": JS(file=HERE / "state.get.js"),
            "state-name": self.name,
        }

    def get(self):
        return Empty(**self.props)

    def set(self, value):
        return JS(
            f"""const state = seamless.state.getState('{self.name}');\
            seamless.state.setState('{self.name}', {value})"""
        )

    def __str__(self):
        return f"seamless.state.getState('{self.name}')"

    @overload
    def __call__(self) -> Any: ...
    @overload
    def __call__(self, value: Any) -> JS: ...

    def __call__(self, value=_EMPTY):
        if value is _EMPTY:
            return self.get()
        return self.set(value)

    def __add__(self, other):
        return self.get() + other

    def __radd__(self, other):
        return other + self.get()

    @staticmethod
    def init():
        class _StateInit(Component):
            def render(self):
                state = {state.name: state.default_value for state in State}
                return Empty(init=JS(file=HERE / "state.init.js"), state=dumps(state))

        return _StateInit()


class StateFeature(Feature):
    def __init__(self, context: "Context"):
        super().__init__(context)
        self.context.add_prop_transformer(*self.state_transformer())

    def state_transformer(self):
        def matcher(_, value):
            return isinstance(value, Empty) and value.props.get("state-name", False)

        def transformer(key, value: Empty, element: ElementNode):
            empty_props = value.props
            element.props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
            element.props[SEAMLESS_INIT_ATTRIBUTE] = (
                element.props.get(SEAMLESS_INIT_ATTRIBUTE, "")
                + f"""document.addEventListener('stateChange:{empty_props["state-name"]}', (event) => {{
                    const state = event.detail;
                    this.setAttribute('{key}', state.currentValue);
                }});
                this.setAttribute('{key}', seamless.state.getState('{empty_props["state-name"]}'));"""
            )

            del element.props[key]

        return matcher, transformer


del _StateMeta
