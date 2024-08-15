from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableSectionElement
    from ..types import ChildType

class TBody(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableSectionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "tbody"
