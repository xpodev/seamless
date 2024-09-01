from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLTitleElement
from ..types import ChildType


class Title(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLTitleElement]): ...
