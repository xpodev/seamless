from os import PathLike
from seamless.rendering.transformers import transformer_for


class JavaScript:
    def __init__(self, code: str = None, *, file: str | PathLike = None) -> None:
        if file:
            if code:
                raise ValueError("Cannot specify both code and file")
            with open(file, "r") as f:
                code = f.read()
        elif not code:
            raise ValueError("Must specify either code or file")
        self.code = code


@transformer_for(lambda key, value: key == "init" and isinstance(value, JavaScript))
def transform_init_source(key: str, source: JavaScript, props):
    props["seamless:element"] = True
    props["seamless:init"] = source.code
    del props[key]


@transformer_for(
    lambda key, value: key.startswith("on_") and isinstance(value, JavaScript)
)
def transform_event_source(key: str, source: JavaScript, props):
    event_name = key.removeprefix("on_")

    props["seamless:element"] = True
    props["seamless:init"] = (
        props.get("seamless:init", "")
        + f"\nthis.addEventListener('{event_name}', (event) => {{{source.code}}});"
    )
    del props[key]


JS = JavaScript
