from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTableDataCellElement
from ..types import ChildType


class Td(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTableDataCellElement]): ...
