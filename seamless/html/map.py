from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLMapElement
    from ..types import ChildType

class Map(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLMapElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "map"
