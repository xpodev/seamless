from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLUnorderedListElement
    from ..types import ChildType

class Ul(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLUnorderedListElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "ul"
