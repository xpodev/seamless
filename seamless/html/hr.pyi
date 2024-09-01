from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLHRElement
from ..types import ChildType


class Hr(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLHRElement]): ...
