from abc import abstractmethod
from typing import TYPE_CHECKING, Final


if TYPE_CHECKING:
    from seamless.types import RenderResult, ChildrenType


class Component:
    children: Final[tuple["ChildrenType", ...]]

    def __init__(self, *children: "ChildrenType") -> None:
        self.children = children

    @abstractmethod
    def render(self) -> "RenderResult":
        raise NotImplementedError(f"{type(self).__name__}.render() is not implemented")

    def __init_subclass__(cls, *, name: str = None, **kwargs) -> None:
        super().__init_subclass__(**kwargs)

        if cls is not Component:
            from ..context.components import COMPONENTS_REPOSITORY

            COMPONENTS_REPOSITORY.add_component(cls, name or cls.__name__)

        if cls.__init__ is Component.__init__:
            return

        original_init = cls.__init__

        def __init__(self, *args, children=None, **kwargs):
            Component.__init__(self, *(getattr(self, "children", children) or args))
            original_init(self, **kwargs)

        cls.__init__ = __init__

    def __call__(self, *children: "ChildrenType"):
        self.children = children
        return self
