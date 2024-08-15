from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLLinkElement
    from ..types import ChildType

class Link(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLLinkElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "link"
    inline = True
