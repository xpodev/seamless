from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLTrackElement(HTMLElementProps, total=False):
    default: str
    kind: str
    label: str
    src: str
    srclang: str
