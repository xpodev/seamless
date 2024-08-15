from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import HTMLDialogElement
    from ..types import ChildType

class Dialog(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["HTMLDialogElement"]):
        super().__init__(*children, **kwargs)

    tag_name = "dialog"
