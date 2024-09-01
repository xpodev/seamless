from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLBRElement
from ..types import ChildType


class Br(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLBRElement]): ...
