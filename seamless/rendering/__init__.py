from typing import TYPE_CHECKING, overload, Literal

from .html import render_html
from .json import render_json

if TYPE_CHECKING:
    from ..types import Renderable, Primitive
    from ..context.base import ContextBase


@overload
def render(
    element: "Renderable | Primitive",
    *,
    to: Literal["html"],
    pretty: bool = False,
    tab_indent: int = 1,
    context: "ContextBase | None" = None,
    **render_state_data,
) -> str: ...


@overload
def render(
    element: "Renderable | Primitive",
    *,
    to: Literal["json"],
    context: "ContextBase | None" = None,
    **render_state_data,
) -> dict: ...


@overload
def render(
    element: "Renderable | Primitive",
    *,
    pretty: bool = False,
    tab_indent: int = 1,
    context: "ContextBase | None" = None,
    **render_state_data,
) -> str: ...


def render(
    element: "Renderable | Primitive",
    *,
    to: Literal["json", "html"] = "html",
    **kwargs,
) -> str | dict:

    if to == "json":
        return render_json(element, **kwargs)
    if to == "html":
        return render_html(element, **kwargs)


__all__ = ["render", "render_html", "render_json"]