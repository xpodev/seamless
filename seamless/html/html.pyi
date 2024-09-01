from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLHtmlElement
from ..types import ChildType


class Html(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLHtmlElement]): ...
