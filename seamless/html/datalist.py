from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDataListElement
    from ..types import ChildType

class DataList(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDataListElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "datalist"
