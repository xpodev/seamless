from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLParagraphElement
    from ..types import ChildType

class P(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLParagraphElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "p"
