from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLBodyElement
from ..types import ChildType


class Body(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLBodyElement]): ...
