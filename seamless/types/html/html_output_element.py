from seamless.types.html.html_element_props import HTMLElementProps


class HTMLOutputElement(HTMLElementProps, total=False):
    html_for: str  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: str
    name: str
