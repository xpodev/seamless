from typing import TYPE_CHECKING

from .tree_node import TreeNode

if TYPE_CHECKING:
    from .element_node import ElementNode
    from ....types import Primitive

class TextNode(TreeNode):
    def __init__(self, text: "Primitive", parent: "ElementNode | None" = None):
        super().__init__(parent=parent)
        self.text = str(text) if text is not None else ""
