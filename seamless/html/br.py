from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLBRElement
    from ..types import ChildType

class Br(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLBRElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "br"
    inline = True
