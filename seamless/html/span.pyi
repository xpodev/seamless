from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLSpanElement
from ..types import ChildType


class Span(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLSpanElement]): ...
