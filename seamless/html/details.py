from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDetailsElement
    from ..types import ChildType

class Details(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDetailsElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "details"
