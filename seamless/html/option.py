from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLOptionElement
    from ..types import ChildType

class Option(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOptionElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "option"
