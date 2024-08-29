from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLSourceElement(HTMLElementProps, total=False):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
