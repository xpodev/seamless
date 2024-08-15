from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLVideoElement
    from ..types import ChildType

class Video(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLVideoElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "video"
