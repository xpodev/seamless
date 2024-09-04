from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTableElement
from ..types import ChildType


class Table(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTableElement]): ...
