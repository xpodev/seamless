from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLEmbedElement
    from ..types import ChildType

class Embed(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLEmbedElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "embed"
    inline = True
