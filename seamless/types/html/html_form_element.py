from seamless.types.html.html_element_props import HTMLElementProps


class HTMLFormElement(HTMLElementProps, total=False):
    accept_charset: str
    action: str
    auto_complete: str
    enctype: str
    method: str
    name: str
    no_validate: str
    target: str
