from html import escape
from typing import Any
from ..errors import RenderError
from .transformers import TRANSFORMERS


def transform_props(props: dict[str, Any]):
    props_copy = props.copy()

    for matcher, transformer in TRANSFORMERS:
        if isinstance(matcher, str):
            key = matcher
            if key in props_copy:
                value = props_copy[key]
                props_copy[key] = None
                if callable(transformer):
                    transformer(key, value, props_copy)
                else:
                    props_copy[transformer] = value
        elif callable(matcher):
            for key, value in list(props_copy.items()):
                if matcher(key, value):
                    transformer(key, value, props_copy)
                    props_copy[key] = None
        else:
            raise RenderError(
                f"Invalid matcher: {matcher} must be a callable or a string."
            )

    return props_copy


def render_props(props: dict[str, Any]) -> str:
    return " ".join(
        key if value is True else f'{key}="{escape(str(value))}"'
        for key, value in props.items()
    )
