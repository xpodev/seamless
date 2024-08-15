from os import PathLike
from typing import overload
from seamless.internal import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE
from seamless.rendering.transformers import transformer_for


class JavaScript:
    @overload
    def __init__(self, code: str) -> None: ...
    @overload
    def __init__(self, *, file: str | PathLike) -> None: ...

    def __init__(self, code=None, *, file=None) -> None:
        if file:
            if code:
                raise ValueError("Cannot specify both code and file")
            with open(file, "r") as f:
                code = f.read()
        elif not code:
            raise ValueError("Must specify either code or file")
        self.code = code

    def __add__(self, other: "JavaScript | str") -> "JavaScript":
        if isinstance(other, JavaScript):
            return JavaScript(self.code + other.code)
        elif isinstance(other, str):
            return JavaScript(self.code + other)
        else:
            raise TypeError(
                f"Cannot concatenate JavaScript with {type(other).__name__}"
            )


@transformer_for(lambda key, value: key == "init" and isinstance(value, JavaScript))
def transform_init_source(key: str, source: JavaScript, props):
    props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
    props[SEAMLESS_INIT_ATTRIBUTE] = props.get(SEAMLESS_INIT_ATTRIBUTE, "") + source.code
    del props[key]


@transformer_for(
    lambda key, value: key.startswith("on_") and isinstance(value, JavaScript)
)
def transform_event_source(key: str, source: JavaScript, props):
    event_name = key.removeprefix("on_")

    props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
    props[SEAMLESS_INIT_ATTRIBUTE] = (
        props.get(SEAMLESS_INIT_ATTRIBUTE, "")
        + f"\nthis.addEventListener('{event_name}', (event) => {{{source.code}}});"
    )
    del props[key]


JS = JavaScript
