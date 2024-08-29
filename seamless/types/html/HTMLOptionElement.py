from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLOptionElement(HTMLElementProps, total=False):
    disabled: str
    label: str
    selected: str
    value: str
