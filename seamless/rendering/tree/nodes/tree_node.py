from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from .element_node import ElementNode

class TreeNode:
    def __init__(self, parent: "ElementNode | None" = None):
        self.parent = parent