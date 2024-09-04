from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLSlotElement
from ..types import ChildType


class Slot(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLSlotElement]): ...
