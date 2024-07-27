from typing import TYPE_CHECKING
from seamless import Element

if TYPE_CHECKING:
    from seamless.types import ChildrenType

class Empty(Element):
    tag_name = "seamless:empty"

    def __init__(self, *args: "ChildrenType", **props: dict):
        props["seamless:element"] = True
        super().__init__(*args, **props)