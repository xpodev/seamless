from seamless.types.html.aria_props import AriaProps
from seamless.types.html.html_element import HTMLElement
from seamless.types.html.html_event_props import HTMLEventProps


class HTMLElementProps(HTMLElement, AriaProps, HTMLEventProps):
    pass
