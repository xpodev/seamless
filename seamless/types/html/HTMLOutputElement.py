from seamless.types.html.HTMLElementProps import HTMLElementProps


class HTMLOutputElement(HTMLElementProps, total=False):
    html_for: str  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: str
    name: str
