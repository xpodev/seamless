from typing import TYPE_CHECKING
from uuid import uuid4 as uuid

from .tree.tree import ElementNode, TreeNode, TextNode

from ..internal.utils import is_primitive

from ..context import Context, get_context
from ..context.request import request as _request
from ..core.component import Component
from ..errors import RenderError
from ..element import Element
from .props import render_props
from .render_state import RenderState
from .tree import build_tree

if TYPE_CHECKING:
    from ..types import Renderable, Primitive


def render(
    element: "Renderable | Primitive",
    *,
    pretty=False,
    tab_indent=1,
    context: Context | None = None,
    **render_state_data,
) -> str:
    """
    Renders the given element into an HTML string.

    Args:
        element (Renderable | Primitive): The element to be rendered.
        pretty (bool, optional): Whether to format the HTML string with indentation and line breaks. Defaults to False.
        tab_indent (int, optional): The number of spaces to use for indentation when pretty is True. Defaults to 1.

    Returns:
        str: The rendered HTML string.
    """

    request = _request()
    if request is not None:
        request.id = str(uuid())

    context = get_context(context)
    render_state = RenderState(**render_state_data)
    context.injector.add(RenderState, render_state)
    return _render(
        element,
        pretty=pretty,
        tab_indent=tab_indent,
        context=context,
        render_state=render_state,
    )


def _render(
    element: "Renderable | Primitive",
    *,
    pretty=False,
    tab_indent=1,
    context: Context,
    render_state: RenderState,
) -> str:
    if is_primitive(element):
        return str(element)

    assert isinstance(element, Component) or isinstance(element, Element)

    tree = build_tree(element, context=context)

    def render_html(node: TreeNode, pretty=False, tab_indent=0):
        tab = "  " * tab_indent if pretty else ""
        newline = "\n" if pretty else ""

        if isinstance(node, TextNode):
            return tab + node.text

        if not isinstance(node, ElementNode):
            raise RenderError("Invalid node type")
        
        props_string = render_props(node.props)
        open_tag = f"{node.tag_name} {props_string}".strip()

        if node.children is None:
            return tab + f"<{open_tag}>"

        children = newline.join(render_html(child, pretty=pretty, tab_indent=tab_indent + 1) for child in node.children)

        if not node.tag_name:
            return tab + children

        return tab + f"<{open_tag}>{newline if children else ''}{children}</{node.tag_name}>"

    return render_html(tree, pretty=pretty, tab_indent=tab_indent)
