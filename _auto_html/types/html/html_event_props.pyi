from typing import Callable, Optional
from typing_extensions import TypedDict

EventHandler = Optional[str] | Callable

class HTMLEventProps(TypedDict, total=False):
    on_abort: EventHandler
    on_auto_complete: EventHandler
    on_auto_complete_error: EventHandler
    on_blur: EventHandler
    on_cancel: EventHandler
    on_can_play: EventHandler
    on_can_play_through: EventHandler
    on_change: EventHandler
    on_click: EventHandler
    on_close: EventHandler
    on_context_menu: EventHandler
    on_cue_change: EventHandler
    on_dbl_click: EventHandler
    on_drag: EventHandler
    on_drag_end: EventHandler
    on_drag_enter: EventHandler
    on_drag_leave: EventHandler
    on_drag_over: EventHandler
    on_drag_start: EventHandler
    on_drop: EventHandler
    on_duration_change: EventHandler
    on_emptied: EventHandler
    on_ended: EventHandler
    on_error: EventHandler
    on_focus: EventHandler
    on_input: EventHandler
    on_invalid: EventHandler
    on_key_down: EventHandler
    on_key_press: EventHandler
    on_key_up: EventHandler
    on_load: EventHandler
    on_loaded_data: EventHandler
    on_loaded_metadata: EventHandler
    on_load_start: EventHandler
    on_mouse_down: EventHandler
    on_mouse_enter: EventHandler
    on_mouse_leave: EventHandler
    on_mouse_move: EventHandler
    on_mouse_out: EventHandler
    on_mouse_over: EventHandler
    on_mouse_up: EventHandler
    on_mouse_wheel: EventHandler
    on_pause: EventHandler
    on_play: EventHandler
    on_playing: EventHandler
    on_progress: EventHandler
    on_rate_change: EventHandler
    on_reset: EventHandler
    on_resize: EventHandler
    on_scroll: EventHandler
    on_seeked: EventHandler
    on_seeking: EventHandler
    on_select: EventHandler
    on_show: EventHandler
    on_sort: EventHandler
    on_stalled: EventHandler
    on_submit: EventHandler
    on_suspend: EventHandler
    on_time_update: EventHandler
    on_toggle: EventHandler
    on_volume_change: EventHandler
    on_waiting: EventHandler