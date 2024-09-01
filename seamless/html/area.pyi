from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLAreaElement
from ..types import ChildType


class Area(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLAreaElement]): ...
