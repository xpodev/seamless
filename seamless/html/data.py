from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDataElement
    from ..types import ChildType

class Data(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDataElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "data"
