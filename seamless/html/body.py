from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLBodyElement
    from ..types import ChildType

class Body(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLBodyElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "body"
