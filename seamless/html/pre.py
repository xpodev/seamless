from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLPreElement
    from ..types import ChildType

class Pre(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLPreElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "pre"
