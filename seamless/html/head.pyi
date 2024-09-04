from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLHeadElement
from ..types import ChildType


class Head(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLHeadElement]): ...
