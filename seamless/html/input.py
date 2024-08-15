from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLInputElement
    from ..types import ChildType

class Input(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLInputElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "input"
    inline = True
