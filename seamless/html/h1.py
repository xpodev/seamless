from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLHeadingElement
    from ..types import ChildType

class H1(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLHeadingElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "h1"
