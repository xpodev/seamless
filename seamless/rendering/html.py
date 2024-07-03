from typing import TYPE_CHECKING
from uuid import uuid4 as uuid

from ..context.request import request as _request
from ..errors import RenderError
from ..components.base import Component
from ..element import Element
from .props import render_props

if TYPE_CHECKING:
    from seamless.types import Renderable, Primitive


def render(element: "Renderable | Primitive", *, pretty=False, tab_indent=1) -> str:
    request = _request()
    if request is not None:
        request.id = str(uuid())
    return _render(element, pretty=pretty, tab_indent=tab_indent)


def _render(element: "Renderable | Primitive", *, pretty=False, tab_indent=1) -> str:
    if isinstance(element, Component):
        element = _render(element.render(), pretty=pretty, tab_indent=tab_indent)

    if not isinstance(element, Element):
        return str(element) if element is not None else ""

    tag_name = getattr(element, "tag_name", None)

    props = {k: v for k, v in element.props_dict().items() if v not in [None, False]}

    props_string = render_props(props)
    open_tag = f"{tag_name} {props_string}".strip()

    if element.inline:
        if len(element.children) > 0:
            # Maybe this should be a warning instead of an error?
            raise RenderError("Inline components cannot have children")
        return f"<{open_tag}>"

    tab = "  " * tab_indent if pretty else ""
    children_join_string = f"\n{tab}" if pretty else ""
    children = [
        _render(child, pretty=pretty, tab_indent=tab_indent + 1)
        for child in element.children
    ]
    if pretty:
        children.insert(0, "")

    children = children_join_string.join(children)

    if pretty:
        children += f"\n{tab[:-2]}"

    if not tag_name:
        return children

    return f"<{open_tag}>{children}</{tag_name}>"
