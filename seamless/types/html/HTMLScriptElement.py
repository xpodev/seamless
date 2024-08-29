from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLScriptElement(HTMLElementProps, total=False):
    async_: bool  # 'async' is a reserved keyword in Python, so using 'async_'
    cross_origin: str
    defer: bool
    integrity: str
    nonce: str
    referrer_policy: str
    src: str
    type: str
