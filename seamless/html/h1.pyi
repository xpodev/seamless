from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLHeadingElement
from ..types import ChildType


class H1(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLHeadingElement]): ...
