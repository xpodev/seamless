from seamless.types.html.html_element_props import HTMLElementProps


class HTMLMeterElement(HTMLElementProps, total=False):
    form: str
    high: str
    low: str
    max: str
    min: str
    optimum: str
    value: str
