from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLStyleElement
    from ..types import ChildType

class Style(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLStyleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "style"
