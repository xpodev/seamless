from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLAnchorElement(HTMLElementProps, total=False):
    download: str
    href: str
    href_lang: str
    ping: str
    referrer_policy: str
    rel: str
    target: str
    type: str
