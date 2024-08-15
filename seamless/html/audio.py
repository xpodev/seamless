from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLAudioElement
    from ..types import ChildType

class Audio(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLAudioElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "audio"
