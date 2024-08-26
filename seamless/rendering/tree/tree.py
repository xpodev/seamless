from typing import TYPE_CHECKING

from ..props import transform_props


from ...core.component import Component
from ...element import Element
from ...errors import RenderError
from ...internal.utils import is_primitive

if TYPE_CHECKING:
    from ...types import Primitive, Renderable
    from ...context import Context


class TreeNode:
    def __init__(self, parent: "ElementNode | None" = None):
        self.parent = parent


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

    def get_by_tag(self, tag: str):
        def _get_by_tag(node: ElementNode) -> ElementNode | None:
            if node.tag_name == tag:
                return node
            if node.children is not None:
                for child in node.children:
                    if isinstance(child, ElementNode):
                        result = _get_by_tag(child)
                        if result:
                            return result
            return None

        return _get_by_tag(self)

    def get_all_by_tag(self, tag: str):
        def _get_all_by_tag(node: ElementNode) -> list[ElementNode]:
            result = []
            if node.tag_name == tag:
                result.append(node)
            if node.children is not None:
                for child in node.children:
                    if isinstance(child, ElementNode):
                        result.extend(_get_all_by_tag(child))
            return result

        return _get_all_by_tag(self)

    def insert_after(self, node: TreeNode):
        if self.parent is None:
            raise RenderError("Cannot insert after root element")

        assert isinstance(self.parent.children, list)

        current_index = self.parent.children.index(self)
        self.parent.children.insert(current_index + 1, node)

    def insert_before(self, node: TreeNode):
        if self.parent is None:
            raise RenderError("Cannot insert before root element")

        assert isinstance(self.parent.children, list)

        current_index = self.parent.children.index(self)
        self.parent.children.insert(current_index, node)

    def insert_child(self, index: int, node: TreeNode):
        if self.children is None:
            raise RenderError("Cannot append child to inline elements")
        
        self.children.insert(index, node)

    def append_child(self, node: TreeNode):
        if self.children is None:
            raise RenderError("Cannot append child to inline elements")
        
        self.children.append(node)


class TextNode(TreeNode):
    def __init__(self, text: "Primitive", parent: ElementNode | None = None):
        super().__init__(parent=parent)
        self.text = str(text) if text is not None else ""


def build_raw_tree(
    renderable: "Renderable | Primitive", *, context: "Context"
) -> TreeNode:
    while isinstance(renderable, Component):
        renderable = renderable.render()

    if is_primitive(renderable):
        return TextNode(renderable)

    assert isinstance(renderable, Element)
    children = (
        [build_raw_tree(child, context=context) for child in renderable.children]
        if not renderable.inline
        else None
    )
    element = ElementNode(
        tag_name=renderable.tag_name, props=renderable.props, children=children
    )

    transform_props(element, context=context)

    return element


def build_tree(renderable: "Renderable | Primitive", *, context: "Context") -> TreeNode:
    tree = build_raw_tree(renderable, context=context)

    if not isinstance(tree, ElementNode):
        return tree

    for transformer in context.post_render_transformers:
        transformer(tree)

    return tree
