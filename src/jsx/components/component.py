from abc import abstractmethod
from typing import TYPE_CHECKING, Final


if TYPE_CHECKING:
    from jsx.types import RenderResult, ChildrenType


class Component:
    @abstractmethod
    def render(self) -> "RenderResult":
        raise NotImplementedError(f"{type(self).__name__}.render() is not implemented")
    
    def __init_subclass__(cls) -> None:
        from jsx.server.components import COMPONENTS_REPOSITORY

        if not getattr(cls.render, "__isabstractmethod__", False):
            COMPONENTS_REPOSITORY.add_component(cls)


class ContainerComponent(Component):
    children: Final[tuple["ChildrenType", ...]]

    def __init__(self, *children: "ChildrenType") -> None:
        self.children = children
