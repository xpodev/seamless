from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLModElement
    from ..types import ChildType

class Ins(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLModElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "ins"
