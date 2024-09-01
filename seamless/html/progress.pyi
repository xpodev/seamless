from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLProgressElement
from ..types import ChildType


class Progress(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLProgressElement]): ...
