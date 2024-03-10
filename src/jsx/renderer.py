from html import escape
from typing import TYPE_CHECKING, Any
from uuid import uuid4 as uuid

from .server.request import request as _request

from .errors import RenderError
from .components.component import Component
from .html.element import Element

if TYPE_CHECKING:
    from .types import Renderable, Primitive


def render(element: "Renderable | Primitive", *, prettify=False, tab_indent=1) -> str:
    request = _request()
    if request is not None:
        request.id = str(uuid())
    return _render(element, prettify=prettify, tab_indent=tab_indent)


def _render(element: "Renderable | Primitive", *, prettify=False, tab_indent=1) -> str:
    if isinstance(element, Component):
        element = _render(element.render(), prettify=prettify, tab_indent=tab_indent)

    if not isinstance(element, Element):
        return str(element) if element is not None else ""

    tag_name = getattr(element, "tag_name", None)

    props = {k: v for k, v in element.props_dict().items() if v not in [None, False]}

    props_string = render_props(props, element)
    open_tag = f"{tag_name} {props_string}".strip()

    if element.inline:
        if len(element.children) > 0:
            # Maybe this should be a warning instead of an error?
            raise RenderError("Inline components cannot have children")
        return f"<{open_tag}>"

    tab = "  " * tab_indent if prettify else ""
    children_join_string = f"\n{tab}" if prettify else ""
    children = [
        _render(child, prettify=prettify, tab_indent=tab_indent + 1)
        for child in element.children
    ]
    if prettify:
        children.insert(0, "")

    children = children_join_string.join(children)

    if prettify:
        children += f"\n{tab[:-2]}"

    if not tag_name:
        return children

    return f"<{open_tag}>{children}</{tag_name}>"


def render_json(element: "Renderable | Primitive"):
    if isinstance(element, Component):
        element = render_json(element.render())

    if not isinstance(element, Element):
        return element

    return {
        "type": element.tag_name,
        "children": list(
            map(
                render_json,
                element.children,
            )
        ),
        "props": element.props_dict(),
    }


def render_props(props: dict[str, Any], element: Element) -> str:
    DB = _db()

    props_strings = []
    for key, value in props.items():
        if callable(value):
            event = key.removeprefix("on_")
            DB.add_element_event(element, event, value)
        elif value is True:
            props_strings.append(key)
        else:
            props_strings.append(f'{key}="{escape(str(value))}"')

    if element in DB.element_ids:
        subscriptable = DB.get_element(element)
        props_strings.append(
            f'jsx:id="{subscriptable.id}" jsx:events="{",".join(subscriptable.events)}"'
        )

    return " ".join(props_strings)


def _db():
    from .server.database import DB

    return DB
