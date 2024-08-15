from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLCanvasElement
    from ..types import ChildType

class Canvas(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLCanvasElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "canvas"
