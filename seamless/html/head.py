from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLHeadElement
    from ..types import ChildType

class Head(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLHeadElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "head"
