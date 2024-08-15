from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLFormElement
    from ..types import ChildType

class Form(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLFormElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "form"
