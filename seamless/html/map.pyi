from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLMapElement
from ..types import ChildType


class Map(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLMapElement]): ...
