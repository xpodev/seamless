from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLImageElement
    from ..types import ChildType

class Img(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLImageElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "img"
    inline = True
