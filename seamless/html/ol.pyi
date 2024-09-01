from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLOrderedListElement
from ..types import ChildType


class Ol(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLOrderedListElement]): ...
