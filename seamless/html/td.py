from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableDataCellElement
    from ..types import ChildType

class Td(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableDataCellElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "td"
