from pathlib import Path
from json import dumps

from seamless.rendering.transformers import transformer_for
from ..javascript import JS
from ..empty import Empty

HERE = Path(__file__).parent

class State:
    def __init__(self, name: str):
        self.name = name
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
    def init(state: dict = None):
        state = state or {}
        return Empty(init=JS(file=HERE / "state.init.js"), state=dumps(state))


@transformer_for(
    lambda _, value: isinstance(value, Empty) and value.props.get("state-name")
)
def transform_state(key, value, props):
    empty_props = value.props
    props["seamless:element"] = True
    props["seamless:init"] = (
        props.get("seamless:init", "")
        + f"""document.addEventListener('stateChange:{empty_props["state-name"]}', (event) => {{
            const state = event.detail;
            this.setAttribute('{key}', state.currentValue);
        }});
        this.setAttribute('{key}', seamless.state.getState('{empty_props["state-name"]}'));"""
    )
    del props[key]
