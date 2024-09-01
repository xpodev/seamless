from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLOptGroupElement
from ..types import ChildType


class OptGroup(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLOptGroupElement]): ...
