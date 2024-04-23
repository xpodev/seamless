from dataclasses import dataclass


try:
    from pydantic import BaseModel
except ImportError:
    @dataclass
    class BaseModel: ...

# region: Event Types

class EventTarget(BaseModel):
    id: str
    tagName: str


class Event(BaseModel):
    type: str
    target: EventTarget


class MouseEvent(Event): ...


class KeyboardEvent(Event): ...


class FormDataEvent(Event): ...


class TouchEvent(Event): ...


class InputEvent(Event): ...


class DragEvent(Event): ...


# endregion
