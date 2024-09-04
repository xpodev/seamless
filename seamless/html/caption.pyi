from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTableCaptionElement
from ..types import ChildType


class Caption(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTableCaptionElement]): ...
