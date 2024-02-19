from html import escape

from .errors import RenderError
from .components.component import Component
from .html.element import Element
from .server import db


def render(
    component: Component | Element | str, *, prettify=False, tab_indent=1
) -> str:
    if isinstance(component, Component):
        component = render(component.render(), prettify=prettify, tab_indent=tab_indent)

    if not isinstance(component, Element):
        return component

    tag_name = getattr(component, "tag_name", None)

    props = {k: v for k, v in component.props_dict().items() if v not in [None, False]}

    props_string = render_props(props, component)
    open_tag = f"{tag_name} {props_string}".strip()

    if component.inline:
        if len(component.children) > 0:
            # Maybe this should be a warning instead of an error?
            raise RenderError("Inline components cannot have children")
        return f"<{open_tag}>"

    tab = "  " * tab_indent if prettify else ""
    children_join_string = f"\n{tab}" if prettify else ""
    children = [
        render(child, prettify=prettify, tab_indent=tab_indent + 1)
        for child in component.children
    ]
    if prettify:
        children.insert(0, "")

    children = children_join_string.join(children)

    if prettify:
        children += f"\n{tab[:-2]}"

    if not tag_name:
        return children

    return f"<{open_tag}>{children}</{tag_name}>"


def render_props(props: dict[str, object], element: Element) -> str:
    props_strings = []
    for key, value in props.items():
        if callable(value):
            event = key.removeprefix("on_")
            db.add_component_event(element, event, value)
        elif value is True:
            props_strings.append(key)
        else:
            props_strings.append(f'{key}="{escape(str(value))}"')

    if element in db.component_ids:
        component_id = db.component_ids[element]
        props_strings.append(
            f'pyx-id="{component_id}" pyx-events="{",".join(db.component_events[component_id].keys())}"'
        )

    return " ".join(props_strings)
