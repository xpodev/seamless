from seamless.types.html.html_element_props import HTMLElementProps


class HTMLTrackElement(HTMLElementProps, total=False):
    default: str
    kind: str
    label: str
    src: str
    srclang: str
