from typing import Callable, TypeVar, TYPE_CHECKING, Union, Concatenate, Iterable
from typing_extensions import TypedDict

if TYPE_CHECKING:
    from ..styling import StyleObject
    from .. import JS

from .events import *

EventProps = TypeVar("EventProps", bound=Event)
EventFunction = Union[Callable[Concatenate[EventProps, ...], None], "JS", str]


class AriaProps(TypedDict, total=False):
    aria_active_descendant: str
    aria_atomic: str
    aria_auto_complete: str
    aria_busy: str
    aria_checked: str
    aria_col_count: str
    aria_col_index: str
    aria_col_span: str
    aria_controls: str
    aria_current: str
    aria_described_by: str
    aria_details: str
    aria_disabled: str
    aria_drop_effect: str
    aria_error_message: str
    aria_expanded: str
    aria_flow_to: str
    aria_grabbed: str
    aria_has_popup: str
    aria_hidden: str
    aria_invalid: str
    aria_key_shortcuts: str
    aria_label: str
    aria_labelled_by: str
    aria_level: str
    aria_live: str
    aria_modal: str
    aria_multiline: str
    aria_multi_selectable: str
    aria_orientation: str
    aria_owns: str
    aria_placeholder: str
    aria_pos_inset: str
    aria_pressed: str
    aria_readonly: str
    aria_relevant: str
    aria_required: str
    aria_role_description: str
    aria_row_count: str
    aria_row_index: str
    aria_row_span: str
    aria_selected: str
    aria_set_size: str
    aria_sort: str
    aria_value_max: str
    aria_value_min: str
    aria_value_now: str
    aria_value_text: str


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


class HTMLElement(TypedDict, total=False, closed=False):
    access_key: str
    auto_capitalize: str
    class_name: str | Iterable[str]
    content_editable: str
    # data: dict[str, str]  # add this if needed in the future
    dir: str
    draggable: str
    hidden: str
    id: str
    input_mode: str
    lang: str
    role: str
    spell_check: str
    style: Union[str, "StyleObject"]
    tab_index: str
    title: str
    translate: str

    init: "JS"


class HTMLElementProps(HTMLElement, AriaProps, HTMLEventProps):
    pass

class HTMLAnchorElement(HTMLElementProps, total=False, closed=False):
    download: str
    href: str
    href_lang: str
    ping: str
    referrer_policy: str
    rel: str
    target: str
    type: str


class HTMLAreaElement(HTMLElementProps, total=False, closed=False):
    alt: str
    coords: str
    download: str
    href: str
    href_lang: str
    ping: str
    referrer_policy: str
    rel: str
    shape: str
    target: str


class HTMLAudioElement(HTMLElementProps, total=False, closed=False):
    auto_play: str
    controls: str
    loop: str
    muted: str
    preload: str
    src: str


class HTMLBRElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLBaseElement(HTMLElementProps, total=False, closed=False):
    href: str
    target: str


class HTMLBodyElement(HTMLElementProps, total=False, closed=False):
    background: str


class HTMLButtonElement(HTMLElementProps, total=False, closed=False):
    auto_focus: str
    disabled: str
    form: str
    form_action: str
    form_enctype: str
    form_method: str
    form_no_validate: str
    form_target: str
    name: str
    type: str
    value: str


class HTMLCanvasElement(HTMLElementProps, total=False, closed=False):
    height: str
    width: str


class HTMLDataElement(HTMLElementProps, total=False, closed=False):
    value: str


class HTMLDataListElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLDetailsElement(HTMLElementProps, total=False, closed=False):
    open: str


class HTMLDialogElement(HTMLElementProps, total=False, closed=False):
    open: str


class HTMLDivElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLEmbedElement(HTMLElementProps, total=False, closed=False):
    height: str
    src: str
    type: str
    width: str


class HTMLFieldSetElement(HTMLElementProps, total=False, closed=False):
    disabled: str
    form: str
    name: str


class HTMLFormElement(HTMLElementProps, total=False, closed=False):
    accept_charset: str
    action: str
    auto_complete: str
    enctype: str
    method: str
    name: str
    no_validate: str
    target: str


class HTMLHRElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLHeadElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLHeadingElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLHtmlElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLIFrameElement(HTMLElementProps, total=False, closed=False):
    allow: str
    allow_fullscreen: str
    csp: str
    frame_border: str
    height: str
    importance: str
    loading: str
    name: str
    referrer_policy: str
    sandbox: str
    scrolling: str
    seamless: str
    src: str
    srcdoc: str
    width: str


class HTMLImageElement(HTMLElementProps, total=False, closed=False):
    alt: str
    cross_origin: str
    decoding: str
    height: str
    importance: str
    intrinsicsize: str
    ismap: str
    loading: str
    referrer_policy: str
    sizes: str
    src: str
    srcset: str
    usemap: str
    width: str


class HTMLInputElement(HTMLElementProps, total=False, closed=False):
    accept: str
    alt: str
    auto_complete: str
    auto_focus: str
    capture: str
    checked: str
    cross_origin: str
    disabled: str
    form: str
    form_action: str
    form_enctype: str
    form_method: str
    form_no_validate: str
    form_target: str
    height: str
    list: str
    max: str
    max_length: str
    min: str
    min_length: str
    multiple: str
    name: str
    pattern: str
    placeholder: str
    readonly: str
    required: str
    selection_direction: str
    selection_end: str
    selection_start: str
    size: str
    src: str
    step: str
    type: str
    value: str
    width: str


class HTMLListItemElement(HTMLElementProps, total=False, closed=False):
    value: str


class HTMLLabelElement(HTMLElementProps, total=False, closed=False):
    html_for: str


class HTMLLegendElement(HTMLElementProps, total=False, closed=False):
    align: str


class HTMLLinkElement(HTMLElementProps, total=False, closed=False):
    html_as: str
    cross_origin: str
    disabled: str
    href: str
    hreflang: str
    media: str
    referrer_policy: str
    rel: str
    sizes: str
    type: str


class HTMLMapElement(HTMLElementProps, total=False, closed=False):
    name: str


class HTMLDocumentMetaElement(HTMLElementProps, total=False, closed=False):
    name: str
    content: str


class HTMLPragmaMetaElement(HTMLElementProps, total=False, closed=False):
    http_equiv: str


class HTMLCharsetMetaElement(HTMLElementProps, total=False, closed=False):
    charset: str


class HTMLUserMetaElement(HTMLElementProps, total=False, closed=False):
    itemprop: str


class HTMLMeterElement(HTMLElementProps, total=False, closed=False):
    form: str
    high: str
    low: str
    max: str
    min: str
    optimum: str
    value: str


class HTMLModElement(HTMLElementProps, total=False, closed=False):
    cite: str
    datetime: str


class HTMLObjectElement(HTMLElementProps, total=False, closed=False):
    data: str
    form: str
    height: str
    name: str
    type: str
    usemap: str
    width: str


class HTMLOrderedListElement(HTMLElementProps, total=False, closed=False):
    reversed: str
    start: str


class HTMLOptGroupElement(HTMLElementProps, total=False, closed=False):
    disabled: str
    label: str


class HTMLOptionElement(HTMLElementProps, total=False, closed=False):
    disabled: str
    label: str
    selected: str
    value: str


class HTMLOutputElement(HTMLElementProps, total=False, closed=False):
    html_for: str  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: str
    name: str


class HTMLParagraphElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLParamElement(HTMLElementProps, total=False, closed=False):
    name: str
    value: str


class HTMLPictureElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLPreElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLProgressElement(HTMLElementProps, total=False, closed=False):
    max: str
    value: str


class HTMLQuoteElement(HTMLElementProps, total=False, closed=False):
    cite: str


class HTMLScriptElement(HTMLElementProps, total=False, closed=False):
    async_: bool  # 'async' is a reserved keyword in Python, so using 'async_'
    cross_origin: str
    defer: bool
    integrity: str
    nonce: str
    referrer_policy: str
    src: str
    type: str


class HTMLSelectElement(HTMLElementProps, total=False, closed=False):
    auto_complete: str
    auto_focus: str
    disabled: str
    form: str
    multiple: str
    name: str
    required: str
    size: str


class HTMLSlotElement(HTMLElementProps, total=False, closed=False):
    name: str


class HTMLSourceElement(HTMLElementProps, total=False, closed=False):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str


class HTMLSpanElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLStyleElement(HTMLElementProps, total=False, closed=False):
    media: str
    nonce: str
    scoped: str


class HTMLTableCaptionElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLTableCellElement(HTMLElementProps, total=False, closed=False):
    abbr: str
    colspan: str
    headers: str
    rowspan: str
    scope: str


class HTMLTableColElement(HTMLElementProps, total=False, closed=False):
    span: str


class HTMLTableDataCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableElement(HTMLElementProps, total=False, closed=False):
    border: str
    cellpadding: str
    cellspacing: str
    frame: str
    rules: str
    summary: str
    width: str


class HTMLTableHeaderCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableRowElement(HTMLElementProps, total=False, closed=False):
    align: str
    bgcolor: str
    ch: str
    choff: str
    v_align: str


class HTMLTableSectionElement(HTMLElementProps, total=False, closed=False):
    align: str
    ch: str
    choff: str
    v_align: str


class HTMLTemplateElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLTextAreaElement(HTMLElementProps, total=False, closed=False):
    auto_complete: str
    auto_focus: str
    cols: str
    dirname: str
    disabled: str
    form: str
    max_length: str
    min_length: str
    name: str
    placeholder: str
    readonly: str
    required: str
    rows: str
    wrap: str


class HTMLTimeElement(HTMLElementProps, total=False, closed=False):
    datetime: str


class HTMLTitleElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLTrackElement(HTMLElementProps, total=False, closed=False):
    default: str
    kind: str
    label: str
    src: str
    srclang: str


class HTMLUnorderedListElement(HTMLElementProps, total=False, closed=False):
    pass  # No additional attributes


class HTMLVideoElement(HTMLElementProps, total=False, closed=False):
    auto_play: str
    controls: str
    cross_origin: str
    height: str
    loop: str
    muted: str
    plays_inline: str
    poster: str
    preload: str
    src: str
    width: str
