from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableElement
    from ..types import ChildType

class Table(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "table"
