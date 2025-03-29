from typing import TYPE_CHECKING, Iterable, Union, Literal

from pydom.styling import StyleSheet
from pydom.types.html.html_element import HTMLElement

if TYPE_CHECKING:
    from seamless.core.javascript import JS


class HTMLElement(HTMLElement, total=False, closed=False):
    init: "JS"
