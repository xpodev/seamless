from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLDataElement
from ..types import ChildType


class Data(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLDataElement]): ...
