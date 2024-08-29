from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLStyleElement(HTMLElementProps, total=False):
    media: str
    nonce: str
    scoped: str
