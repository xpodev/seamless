from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLQuoteElement
    from ..types import ChildType

class Q(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLQuoteElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "q"
