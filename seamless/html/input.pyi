from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLInputElement
from ..types import ChildType


class Input(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLInputElement]): ...
