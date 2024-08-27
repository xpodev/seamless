from .tree_node import TreeNode


class ElementNode(TreeNode):
    def __init__(
        self,
        tag_name: str,
        props: dict | None = None,
        children: list[TreeNode] | None = None,
        parent: "ElementNode | None" = None,
    ):
        super().__init__(parent=parent)
        self.tag_name = tag_name
        self.props = dict(props or ())
        self.children = children
