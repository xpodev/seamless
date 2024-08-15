from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLOutputElement
    from ..types import ChildType

class Output(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOutputElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "output"
