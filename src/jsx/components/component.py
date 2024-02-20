from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar, Final

if TYPE_CHECKING:
    from ..html.element import Element


T = TypeVar("T")


class Component:
    @abstractmethod
    def render(self) -> "Element | str":
        raise NotImplementedError(f"{type(self).__name__}.render() is not implemented")


class ContainerComponent(Component, Generic[T]):
    children: Final[tuple[T, ...]]

    def __init__(self, *children: T) -> None:
        self.children = children
