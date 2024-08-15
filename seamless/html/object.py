from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLObjectElement
    from ..types import ChildType

class Object(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLObjectElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "object"
