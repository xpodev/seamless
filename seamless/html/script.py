from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLScriptElement
    from ..types import ChildType

class Script(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLScriptElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "script"
