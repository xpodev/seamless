from .aria_props import AriaProps
from .html_element import HTMLElement
from .html_event_props import HTMLEventProps


class HTMLElementProps(HTMLElement, AriaProps, HTMLEventProps):
    pass
