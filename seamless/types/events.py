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
    tagName: str


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


class HashChangeEvent(Event): ...


class HIDInputReportEvent(Event): ...


class IDBVersionChangeEvent(Event): ...


class InputEvent(Event): ...


class KeyboardEvent(Event): ...


class MessageEvent(Event): ...


class MouseEvent(Event): ...


class OfflineAudioCompletionEvent(Event): ...


class PageTransitionEvent(Event): ...


class PaymentRequestUpdateEvent(Event): ...


class PointerEvent(Event): ...


class PopStateEvent(Event): ...


class ProgressEvent(Event): ...


class RTCDataChannelEvent(Event): ...


class RTCPeerConnectionIceEvent(Event): ...


class StorageEvent(Event): ...


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