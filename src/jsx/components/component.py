from abc import abstractmethod
from typing import TYPE_CHECKING, Generic, TypeVar, Final


if TYPE_CHECKING:
    from ..html.element import Element


T = TypeVar("T")


class Component:
    @abstractmethod
    def render(self) -> "Element | str":
        raise NotImplementedError(f"{type(self).__name__}.render() is not implemented")
    
    def __init_subclass__(cls) -> None:
        from jsx.server.components import COMPONENTS_REPOSITORY

        if not getattr(cls.render, "__isabstractmethod__", False):
            COMPONENTS_REPOSITORY.add_component(cls)


class ContainerComponent(Component, Generic[T]):
    children: Final[tuple[T, ...]]

    def __init__(self, *children: T) -> None:
        self.children = children
