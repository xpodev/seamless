from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLMeterElement(HTMLElementProps, total=False):
    form: str
    high: str
    low: str
    max: str
    min: str
    optimum: str
    value: str
