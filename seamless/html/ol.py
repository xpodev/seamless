from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLOrderedListElement
    from ..types import ChildType

class Ol(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOrderedListElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "ol"
