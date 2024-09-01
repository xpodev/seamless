from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLImageElement
from ..types import ChildType


class Img(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLImageElement]): ...
