from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLFieldSetElement
from ..types import ChildType


class FieldSet(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLFieldSetElement]): ...
