from typing import TYPE_CHECKING
from seamless import Element
from seamless.internal import SEAMLESS_ELEMENT_ATTRIBUTE

if TYPE_CHECKING:
    from seamless.types import ChildrenType

class Empty(Element):
    tag_name = "seamless:empty"

    def __init__(self, *args: "ChildrenType", **props: dict):
        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        super().__init__(*args, **props)