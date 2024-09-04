from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTimeElement
from ..types import ChildType


class Time(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTimeElement]): ...
