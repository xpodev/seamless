from seamless.types.html.html_element_props import HTMLElementProps


class HTMLSourceElement(HTMLElementProps, total=False):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str
