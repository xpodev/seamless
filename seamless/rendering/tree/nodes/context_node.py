from ....errors import RenderError
from ....context.base import ContextBase
from ....types import Renderable, Primitive

from .element_node import ElementNode


class ContextNode:
    def __init__(self, node: ElementNode, context: ContextBase):
        self.node = node
        self.context = context

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

        node = _get_by_tag(self.node)
        return ContextNode(node, context=self.context) if node else None

    def get_all_by_tag(self, tag: str):
        def _get_all_by_tag(node: ElementNode) -> list[ContextNode]:
            result: list[ContextNode] = []
            if node.tag_name == tag:
                result.append(ContextNode(node, context=self.context))
            if node.children is not None:
                result.extend(
                    [
                        ContextNode(child, context=self.context)
                        for child in node.children
                        if isinstance(child, ElementNode)
                    ]
                )
            return result

        return _get_all_by_tag(self.node)

    def insert_after(self, node: Renderable | Primitive):
        if self.parent is None:
            raise RenderError("Cannot insert after root element")

        assert isinstance(self.parent.children, list)

        current_index = self.parent.children.index(self.node)

        self.parent.children.insert(
            current_index + 1, self._build(node)
        )

    def insert_before(self, node: Renderable | Primitive):
        if self.parent is None:
            raise RenderError("Cannot insert before root element")

        assert isinstance(self.parent.children, list)

        current_index = self.parent.children.index(self.node)
        self.parent.children.insert(
            current_index, self._build(node)
        )

    def insert_child(self, index: int, node: Renderable | Primitive):
        if self.children is None:
            raise RenderError("Cannot append child to inline elements")

        self.children.insert(index, self._build(node))

    def append_child(self, node: Renderable | Primitive):
        if self.children is None:
            raise RenderError("Cannot append child to inline elements")

        self.children.append(self._build(node))

    @property
    def children(self):
        return self.node.children

    @property
    def parent(self):
        return self.node.parent

    @property
    def props(self):
        return self.node.props

    def _build(self, renderable: Renderable | Primitive):
        from ..tree import build_raw_tree
        return build_raw_tree(renderable, context=self.context)
