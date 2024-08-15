from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableCaptionElement
    from ..types import ChildType

class Caption(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableCaptionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "caption"
