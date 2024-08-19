from functools import partial
from typing import TYPE_CHECKING


from ..core.component import Component
from ..element import Element
from ..internal.injector import injector
from .props import transform_props
from .render_state import RenderState

if TYPE_CHECKING:
    from ..types import Renderable, Primitive
    from ..context import Context


def to_dict(element: "Renderable | Primitive", *, context: "Context | None" = None, **render_state_data):
    from ..context import get_context

    render_state = RenderState(**render_state_data)
    injector().add(RenderState, render_state)

    return _to_dict(element, context=get_context(context), render_state=render_state)


def _to_dict(element: "Renderable | Primitive", *, context: "Context", render_state: RenderState):
    if isinstance(element, Component):
        element = _to_dict(element.render(), context=context, render_state=render_state) # type: ignore

    if not isinstance(element, Element):
        return element

    return {
        "type": element.tag_name,
        "children": list(
            map(
                partial(_to_dict, context=context, render_state=render_state),
                element.children,
            )
        ),
        "props": transform_props(element.props, context=context),
    }
