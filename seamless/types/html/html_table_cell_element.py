from seamless.types.html.html_element_props import HTMLElementProps


class HTMLTableCellElement(HTMLElementProps, total=False):
    abbr: str
    colspan: str
    headers: str
    rowspan: str
    scope: str
