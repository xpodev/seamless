from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLSlotElement
    from ..types import ChildType

class Slot(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLSlotElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "slot"
