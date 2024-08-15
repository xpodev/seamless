from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLBaseElement
    from ..types import ChildType

class Base(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLBaseElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "base"
    inline = True
