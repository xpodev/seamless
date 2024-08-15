from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLLegendElement
    from ..types import ChildType

class Legend(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLLegendElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "legend"
