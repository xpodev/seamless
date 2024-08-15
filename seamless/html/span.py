from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLSpanElement
    from ..types import ChildType

class Span(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSpanElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "span"
