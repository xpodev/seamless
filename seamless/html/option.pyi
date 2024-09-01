from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLOptionElement
from ..types import ChildType


class Option(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLOptionElement]): ...
