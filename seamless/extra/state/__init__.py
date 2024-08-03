from pathlib import Path
from json import dumps

from seamless.internal import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE
from seamless.rendering.transformers import transformer_for
from ..javascript import JS
from ..empty import Empty

HERE = Path(__file__).parent


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


@transformer_for(
    lambda _, value: isinstance(value, Empty) and value.props.get("state-name")
)
def transform_state(key, value, props):
    empty_props = value.props
    props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
    props[SEAMLESS_INIT_ATTRIBUTE] = (
        props.get(SEAMLESS_INIT_ATTRIBUTE, "")
        + f"""document.addEventListener('stateChange:{empty_props["state-name"]}', (event) => {{
            const state = event.detail;
            this.setAttribute('{key}', state.currentValue);
        }});
        this.setAttribute('{key}', seamless.state.getState('{empty_props["state-name"]}'));"""
    )
    del props[key]

del _StateMeta