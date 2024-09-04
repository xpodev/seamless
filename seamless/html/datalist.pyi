from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLDataListElement
from ..types import ChildType


class DataList(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLDataListElement]): ...
