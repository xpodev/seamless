from typing import TYPE_CHECKING

from ..core.component import Component
from ..element import Element
from .props import transform_props

if TYPE_CHECKING:
    from ..types import Renderable, Primitive
    from ..context import Context


def to_dict(element: "Renderable | Primitive", *, context: "Context | None" = None):
    from ..context import get_context

    return _to_dict(element, context=get_context(context))


def _to_dict(element: "Renderable | Primitive", *, context: "Context"):
    if isinstance(element, Component):
        element = _to_dict(element.render(), context=context)

    if not isinstance(element, Element):
        return element

    return {
        "type": element.tag_name,
        "children": list(
            map(
                to_dict,
                element.children,
            )
        ),
        "props": transform_props(element.props, context=context),
    }
