from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDivElement
    from ..types import ChildType

class Div(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDivElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "div"
