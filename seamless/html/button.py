from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLButtonElement
    from ..types import ChildType

class Button(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLButtonElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "button"
