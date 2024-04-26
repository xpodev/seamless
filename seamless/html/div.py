from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDivElement
    from ..types import ChildrenType

class Div(Element):
    def __init__(self, *children: "ChildrenType", **kwargs: Unpack["HTMLDivElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "div"
