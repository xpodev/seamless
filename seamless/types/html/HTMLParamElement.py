from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLParamElement(HTMLElementProps, total=False):
    name: str
    value: str
