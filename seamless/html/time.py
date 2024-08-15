from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTimeElement
    from ..types import ChildType

class Time(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTimeElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "time"
