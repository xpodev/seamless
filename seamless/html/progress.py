from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLProgressElement
    from ..types import ChildType

class Progress(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLProgressElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "progress"
