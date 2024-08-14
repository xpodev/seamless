from dataclasses import dataclass
from typing import Generic, TypeVar

try:
    from pydantic import BaseModel
except ImportError:
    @dataclass
    class BaseModel: ...

T = TypeVar("T")

# region: Event Types

class EventTarget(BaseModel):
    id: str
    tagName: str


class Event(BaseModel):
    type: str


class MouseEvent(Event): ...


class KeyboardEvent(Event): ...


class SubmitEvent(Event, Generic[T]):
    data: T


class TouchEvent(Event): ...


class InputEvent(Event): ...


class DragEvent(Event): ...


# endregion
