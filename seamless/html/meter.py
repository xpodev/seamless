from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLMeterElement
    from ..types import ChildType

class Meter(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLMeterElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "meter"
