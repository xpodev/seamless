from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLDivElement
from ..types import ChildType


class Div(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLDivElement]): ...
