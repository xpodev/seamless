from typing import Protocol, TypeAlias

Primitive: TypeAlias = str | int | float | bool | None


class Renderable(Protocol):
    def render(self) -> "RenderResult": ...


ChildrenType: TypeAlias = Renderable | list[Renderable] | Primitive | list[Primitive]
RenderResult: TypeAlias = Renderable | Primitive
