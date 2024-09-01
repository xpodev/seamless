from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLModElement
from ..types import ChildType


class Ins(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLModElement]): ...
