from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLLabelElement
from ..types import ChildType


class Label(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLLabelElement]): ...
