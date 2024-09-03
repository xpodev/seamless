from json import dumps
from pathlib import Path
from typing import Any, overload

from pydom import Component
from pydom.context import Context
from pydom.rendering.tree.nodes import ContextNode

from ...core import Empty, JS
from ..feature import Feature
from ...internal.constants import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE

HERE = Path(__file__).parent
_EMPTY = object()


class _StateMeta(type):
    _instances = {}

    def __call__(self, name: str, *args: Any, **kwds: Any):
        return self._instances.setdefault(name, super().__call__(name, *args, **kwds))

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
    def __init__(self, context: Context):
        super().__init__(context)
        self.context.add_prop_transformer(*self.state_transformer())

    def state_transformer(self):
        def matcher(_, value):
            return isinstance(value, Empty) and value.props.get("state-name", False)

        def transformer(key, value: Empty, element: ContextNode):
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
