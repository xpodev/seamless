from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLFormElement
from ..types import ChildType


class Form(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLFormElement]): ...
