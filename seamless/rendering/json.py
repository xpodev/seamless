from typing import TYPE_CHECKING

from ..components import Component
from ..element import Element

if TYPE_CHECKING:
    from seamless.types import Renderable, Primitive

def to_dict(element: "Renderable | Primitive"):
    if isinstance(element, Component):
        element = to_dict(element.render())

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
        "props": element.props_dict(),
    }

