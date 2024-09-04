from dataclasses import dataclass
from typing import Generic, TypeVar

try:
    from pydantic import BaseModel  # type: ignore
except ImportError:

    @dataclass
    class BaseModel: ...


T = TypeVar("T")

# region: Event Types


class EventTarget(BaseModel):
    id: str
    tag_name: str


class Event(BaseModel):
    type: str


class AnimationEvent(Event): ...


class BeforeUnloadEvent(Event): ...


class BlobEvent(Event): ...


class ClipboardEvent(Event): ...


class CloseEvent(Event): ...


class CompositionEvent(Event): ...


class CustomEvent(Event): ...


class DeviceMotionEvent(Event): ...


class DeviceOrientationEvent(Event): ...


class DragEvent(Event): ...


class ErrorEvent(Event): ...


class FetchEvent(Event): ...


class FocusEvent(Event): ...


class FontFaceSetLoadEvent(Event): ...


class FormDataEvent(Event): ...


class GamepadEvent(Event): ...


class HashChangeEvent(Event):
    old_url: str
    new_url: str


class HIDInputReportEvent(Event): ...


class IDBVersionChangeEvent(Event): ...


class InputEvent(Event): ...


class KeyboardEvent(Event): ...


class MessageEvent(Event):
    data: str
    origin: str
    last_event_id: str
    source: EventTarget
    ports: list


class MouseEvent(Event): ...


class OfflineAudioCompletionEvent(Event): ...


class PageTransitionEvent(Event): ...


class PaymentRequestUpdateEvent(Event): ...


class PointerEvent(Event): ...


class PopStateEvent(Event):
    state: dict | None


class ProgressEvent(Event): ...


class RTCDataChannelEvent(Event): ...


class RTCPeerConnectionIceEvent(Event): ...


class StorageEvent(Event):
    key: str
    old_value: str
    new_value: str
    url: str


class SubmitEvent(Event, Generic[T]):
    data: T


class TimeEvent(Event): ...


class TouchEvent(Event): ...


class TrackEvent(Event): ...


class TransitionEvent(Event): ...


class UIEvent(Event): ...


class WebGLContextEvent(Event): ...


class WheelEvent(Event): ...


# endregion


__all__ = [
    "EventTarget",
    "Event",
    "AnimationEvent",
    "BeforeUnloadEvent",
    "BlobEvent",
    "ClipboardEvent",
    "CloseEvent",
    "CompositionEvent",
    "CustomEvent",
    "DeviceMotionEvent",
    "DeviceOrientationEvent",
    "DragEvent",
    "ErrorEvent",
    "FetchEvent",
    "FocusEvent",
    "FontFaceSetLoadEvent",
    "FormDataEvent",
    "GamepadEvent",
    "HashChangeEvent",
    "HIDInputReportEvent",
    "IDBVersionChangeEvent",
    "InputEvent",
    "KeyboardEvent",
    "MessageEvent",
    "MouseEvent",
    "OfflineAudioCompletionEvent",
    "PageTransitionEvent",
    "PaymentRequestUpdateEvent",
    "PointerEvent",
    "PopStateEvent",
    "ProgressEvent",
    "RTCDataChannelEvent",
    "RTCPeerConnectionIceEvent",
    "StorageEvent",
    "SubmitEvent",
    "TimeEvent",
    "TouchEvent",
    "TrackEvent",
    "TransitionEvent",
    "UIEvent",
    "WebGLContextEvent",
    "WheelEvent",
]
