from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLCanvasElement
from ..types import ChildType


class Canvas(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLCanvasElement]): ...
