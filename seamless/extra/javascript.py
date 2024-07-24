from ..internal import short_uuid
from seamless.rendering.transformers import transformer_for


class JavaScript:
    def __init__(self, code: str) -> None:
        self.code = code
        self.id = short_uuid()
        self.rendered = False

    def render(self) -> str:
        if self.rendered:
            return f"{self.id}()"

        self.rendered = True
        return f"function {self.id}(){{{self.code}}}"


@transformer_for(lambda key, value: key == "init" and isinstance(value, JavaScript))
def transform_init_source(key: str, source: JavaScript, props):
    props["seamless:element"] = True
    props["seamless:id"] = source.id
    props["seamless:init"] = source.code
    del props[key]


@transformer_for(lambda key, value: key.startswith("on_") and isinstance(value, JavaScript))
def transform_event_source(key: str, source: JavaScript, props):
    event_name = key.removeprefix("on_")

    props["seamless:element"] = True
    props["seamless:init"] = props.get("seamless:init", "") + f"\n{source.code}"
    del props[key]


JS = JavaScript