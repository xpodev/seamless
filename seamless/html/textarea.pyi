from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTextAreaElement
from ..types import ChildType


class TextArea(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTextAreaElement]): ...
