from seamless.types.html.html_element_props import HTMLElementProps


class HTMLProgressElement(HTMLElementProps, total=False):
    max: str
    value: str
