from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLParamElement
    from ..types import ChildType

class Param(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLParamElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "param"
    inline = True
