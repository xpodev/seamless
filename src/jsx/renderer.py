from html import escape

from .errors import RenderError
from .components.component import Component
from .html.element import Element
from .server import db


def render(component: Element | str) -> str:
    if isinstance(component, Component):
        component = component.render()

    if not isinstance(component, Element):
        return component

    tag_name = getattr(component, "tag_name", None)
    children = "".join([render(child) for child in component.children])

    if not tag_name:
        return children

    props = {k: v for k, v in component.props.items() if v not in [None, False]}

    if component.inline:
        if component.children != []:
            raise RenderError("Inline components cannot have children")
        return f"<{tag_name} {render_props(props)}/>"

    props_string = render_props(props, component)
    if props_string != "":
        props_string = " " + props_string

    return f"<{tag_name}{props_string}>{children}</{tag_name}>"


def render_props(props: dict[str, object], element: Element) -> str:
    props_string = ""
    for key, value in props.items():
        if callable(value):
            event = key.removeprefix("on_")
            db.add_component_event(element, event, value)
        elif value is True:
            props_string += f"{key} "
        else:
            props_string += f'{key}="{escape(str(value))}" '

    if element in db.component_ids:
        component_id = db.component_ids[element]
        props_string += f'pyx-id="{component_id}" pyx-events="{",".join(db.component_events[component_id].keys())}"'

    return props_string
