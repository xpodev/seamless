from seamless.types.html.html_element_props import HTMLElementProps


class HTMLOptionElement(HTMLElementProps, total=False):
    disabled: str
    label: str
    selected: str
    value: str
