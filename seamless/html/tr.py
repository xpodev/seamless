from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTableRowElement
    from ..types import ChildType

class Tr(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTableRowElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "tr"
