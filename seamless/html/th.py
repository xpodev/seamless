from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableHeaderCellElement
    from ..types import ChildType

class Th(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableHeaderCellElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "th"
