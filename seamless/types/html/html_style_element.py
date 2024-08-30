from seamless.types.html.html_element_props import HTMLElementProps


class HTMLStyleElement(HTMLElementProps, total=False):
    media: str
    nonce: str
    scoped: str
