from seamless.types.html.html_element_props import HTMLElementProps


class HTMLParamElement(HTMLElementProps, total=False):
    name: str
    value: str
