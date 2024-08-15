from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTitleElement
    from ..types import ChildType

class Title(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTitleElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "title"
