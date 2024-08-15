from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLOptGroupElement
    from ..types import ChildType

class OptGroup(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLOptGroupElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "optgroup"
