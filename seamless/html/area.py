from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLAreaElement
    from ..types import ChildType

class Area(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLAreaElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "area"
    inline = True
