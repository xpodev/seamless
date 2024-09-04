from typing import TYPE_CHECKING, Callable, Concatenate, TypeVar, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from seamless.core.javascript import JS

from seamless.types.events import (
    CloseEvent,
    DragEvent,
    ErrorEvent,
    Event,
    FocusEvent,
    KeyboardEvent,
    MouseEvent,
    ProgressEvent,
    SubmitEvent,
    UIEvent,
    WheelEvent,
)

EventProps = TypeVar("EventProps", bound=Event)
EventFunction = Union[Callable[Concatenate[EventProps, ...], None], "JS", str]


class HTMLEventProps(TypedDict, total=False):
    on_abort: EventFunction[Event]
    on_auto_complete: EventFunction[Event]
    on_auto_complete_error: EventFunction[Event]
    on_blur: EventFunction[FocusEvent]
    on_cancel: EventFunction[Event]
    on_can_play: EventFunction[Event]
    on_can_play_through: EventFunction[Event]
    on_change: EventFunction[Event]
    on_click: EventFunction[MouseEvent]
    on_close: EventFunction[CloseEvent]
    on_context_menu: EventFunction[MouseEvent]
    on_cue_change: EventFunction[Event]
    on_dbl_click: EventFunction[MouseEvent]
    on_drag: EventFunction[DragEvent]
    on_drag_end: EventFunction[DragEvent]
    on_drag_enter: EventFunction[DragEvent]
    on_drag_leave: EventFunction[DragEvent]
    on_drag_over: EventFunction[DragEvent]
    on_drag_start: EventFunction[DragEvent]
    on_drop: EventFunction[DragEvent]
    on_duration_change: EventFunction[Event]
    on_emptied: EventFunction[Event]
    on_ended: EventFunction[Event]
    on_error: EventFunction[ErrorEvent]
    on_focus: EventFunction[FocusEvent]
    on_input: EventFunction[Event]
    on_invalid: EventFunction[Event]
    on_key_down: EventFunction[KeyboardEvent]
    on_key_press: EventFunction[KeyboardEvent]
    on_key_up: EventFunction[KeyboardEvent]
    on_load: EventFunction[Event]
    on_loaded_data: EventFunction[Event]
    on_loaded_metadata: EventFunction[Event]
    on_load_start: EventFunction[Event]
    on_mouse_down: EventFunction[MouseEvent]
    on_mouse_enter: EventFunction[MouseEvent]
    on_mouse_leave: EventFunction[MouseEvent]
    on_mouse_move: EventFunction[MouseEvent]
    on_mouse_out: EventFunction[MouseEvent]
    on_mouse_over: EventFunction[MouseEvent]
    on_mouse_up: EventFunction[MouseEvent]
    on_mouse_wheel: EventFunction[WheelEvent]
    on_pause: EventFunction[Event]
    on_play: EventFunction[Event]
    on_playing: EventFunction[Event]
    on_progress: EventFunction[ProgressEvent]
    on_rate_change: EventFunction[Event]
    on_reset: EventFunction[Event]
    on_resize: EventFunction[UIEvent]
    on_scroll: EventFunction[UIEvent]
    on_seeked: EventFunction[Event]
    on_seeking: EventFunction[Event]
    on_select: EventFunction[Event]
    on_show: EventFunction[Event]
    on_sort: EventFunction[Event]
    on_stalled: EventFunction[Event]
    on_submit: EventFunction[SubmitEvent]
    on_suspend: EventFunction[Event]
    on_time_update: EventFunction[Event]
    on_toggle: EventFunction[Event]
    on_volume_change: EventFunction[Event]
    on_waiting: EventFunction[Event]
