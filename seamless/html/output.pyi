from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLOutputElement
from ..types import ChildType


class Output(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLOutputElement]): ...
