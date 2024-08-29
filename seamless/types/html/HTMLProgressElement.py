from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLProgressElement(HTMLElementProps, total=False):
    max: str
    value: str
