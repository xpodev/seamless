from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLLabelElement
    from ..types import ChildType

class Label(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLLabelElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "label"
