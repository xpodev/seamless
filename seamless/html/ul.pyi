from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLUnorderedListElement
from ..types import ChildType


class Ul(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLUnorderedListElement]): ...
