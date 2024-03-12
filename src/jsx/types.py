from typing import Protocol, TypeAlias, TYPE_CHECKING

if TYPE_CHECKING:
    from . import Component, Element

Primitive: TypeAlias = str | int | float | bool | None


class Renderable(Protocol):
    def render(self) -> "RenderResult": ...


ChildrenType: TypeAlias = Renderable | list[Renderable] | Primitive | list[Primitive]
RenderResult: TypeAlias = Renderable | Primitive


class JSXEvent:
    target: "Component | Element"


class JSXMouseEvent(JSXEvent):
    ...


class JSXKeyboardEvent(JSXEvent):
    ...


class JSXFormDataEvent(JSXEvent):
    ...


class JSXTouchEvent(JSXEvent):
    ...


class JSXInputEvent(JSXEvent):
    ...


class JSXDragEvent(JSXEvent):
    ...