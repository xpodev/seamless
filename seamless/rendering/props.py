from html import escape
from typing import Any, TYPE_CHECKING
from ..errors import RenderError

if TYPE_CHECKING:
    from ..context import Context


def transform_props(props: dict[str, Any], *, context: "Context"):
    props_copy = props.copy()

    for matcher, transformer in context._prop_transformers:
        if isinstance(matcher, str):
            key = matcher
            if key in props_copy:
                value = props_copy[key]
                if callable(transformer):
                    transformer(key, value, props_copy)
                else:
                    props_copy[transformer] = value
        elif callable(matcher):
            for key, value in list(props_copy.items()):
                if matcher(key, value):
                    transformer(key, value, props_copy)
        else:
            raise RenderError(
                f"Invalid matcher: {matcher} must be a callable or a string."
            )

    return {
        key: value
        for key, value in props_copy.items()
        if value is not None
    }


def render_props(props: dict[str, Any]) -> str:
    return " ".join(
        key if value is True else f'{key}="{escape(str(value))}"'
        for key, value in props.items()
    )
