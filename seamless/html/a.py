from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLAnchorElement
    from ..types import ChildType

class A(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLAnchorElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "a"
