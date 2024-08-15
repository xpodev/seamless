from typing import TYPE_CHECKING, Any
from seamless.element import Element
from seamless.internal import SEAMLESS_ELEMENT_ATTRIBUTE

if TYPE_CHECKING:
    from seamless.types import ChildType

class Empty(Element):
    tag_name = "seamless:empty"

    def __init__(self, *args: "ChildType", **props: Any):
        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        super().__init__(*args, **props)
