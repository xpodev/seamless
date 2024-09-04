from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLBaseElement
from ..types import ChildType


class Base(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLBaseElement]): ...
