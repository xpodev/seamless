from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLTrackElement
    from ..types import ChildType

class Track(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLTrackElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "track"
    inline = True
