from typing import TYPE_CHECKING, Any
from ..element import Element
from ..internal.constants import SEAMLESS_ELEMENT_ATTRIBUTE

if TYPE_CHECKING:
    from ..types import ChildType

class Empty(Element):
    tag_name = "seamless:empty"

    def __init__(self, *args: "ChildType", **props: Any):
        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        super().__init__(*args, **props)
