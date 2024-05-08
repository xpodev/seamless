from typing import TYPE_CHECKING, TypeVar, Generic, Unpack
from abc import abstractmethod

from .rendering.props import transform_props

if TYPE_CHECKING:
    from seamless.types import ChildrenType


PropsType = TypeVar("PropsType")


class Element(Generic[PropsType]):
    def __init__(
        self,
        *args: "ChildrenType",
        children: "ChildrenType" = None,
        **kwargs: Unpack[PropsType],
    ):
        self.children = tuple(children or args)
        self.props = kwargs

    @property
    @abstractmethod
    def tag_name(self) -> str:
        pass

    inline = False

    def props_dict(self):
        return transform_props(self.props)

    def __call__(self, *children: "ChildrenType"):
        self.children = children
        return self
