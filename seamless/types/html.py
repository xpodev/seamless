from typing import TypedDict, Callable, TypeVar, NotRequired, TYPE_CHECKING

if TYPE_CHECKING:
    from ..styling import StyleObject
    from .. import JS

from .events import Event, MouseEvent

EventProps = TypeVar("EventProps", bound=Event)
EventFunction = Callable[[EventProps], None]


class AriaProps(TypedDict):
    aria_active_descendant: NotRequired[str]
    aria_atomic: NotRequired[str]
    aria_auto_complete: NotRequired[str]
    aria_busy: NotRequired[str]
    aria_checked: NotRequired[str]
    aria_col_count: NotRequired[str]
    aria_col_index: NotRequired[str]
    aria_col_span: NotRequired[str]
    aria_controls: NotRequired[str]
    aria_current: NotRequired[str]
    aria_described_by: NotRequired[str]
    aria_details: NotRequired[str]
    aria_disabled: NotRequired[str]
    aria_drop_effect: NotRequired[str]
    aria_error_message: NotRequired[str]
    aria_expanded: NotRequired[str]
    aria_flow_to: NotRequired[str]
    aria_grabbed: NotRequired[str]
    aria_has_popup: NotRequired[str]
    aria_hidden: NotRequired[str]
    aria_invalid: NotRequired[str]
    aria_key_shortcuts: NotRequired[str]
    aria_label: NotRequired[str]
    aria_labelled_by: NotRequired[str]
    aria_level: NotRequired[str]
    aria_live: NotRequired[str]
    aria_modal: NotRequired[str]
    aria_multiline: NotRequired[str]
    aria_multi_selectable: NotRequired[str]
    aria_orientation: NotRequired[str]
    aria_owns: NotRequired[str]
    aria_placeholder: NotRequired[str]
    aria_pos_inset: NotRequired[str]
    aria_pressed: NotRequired[str]
    aria_readonly: NotRequired[str]
    aria_relevant: NotRequired[str]
    aria_required: NotRequired[str]
    aria_role_description: NotRequired[str]
    aria_row_count: NotRequired[str]
    aria_row_index: NotRequired[str]
    aria_row_span: NotRequired[str]
    aria_selected: NotRequired[str]
    aria_set_size: NotRequired[str]
    aria_sort: NotRequired[str]
    aria_value_max: NotRequired[str]
    aria_value_min: NotRequired[str]
    aria_value_now: NotRequired[str]
    aria_value_text: NotRequired[str]


class HTMLEventProps(TypedDict):
    on_abort: NotRequired[str]
    on_auto_complete: NotRequired[str]
    on_auto_complete_error: NotRequired[str]
    on_blur: NotRequired[str]
    on_cancel: NotRequired[str]
    on_can_play: NotRequired[str]
    on_can_play_through: NotRequired[str]
    on_change: NotRequired[str]
    on_click: EventFunction[MouseEvent]
    on_close: NotRequired[str]
    on_context_menu: EventFunction[MouseEvent]
    on_cue_change: NotRequired[str]
    on_dbl_click: EventFunction[MouseEvent]
    on_drag: NotRequired[str]
    on_drag_end: NotRequired[str]
    on_drag_enter: NotRequired[str]
    on_drag_leave: NotRequired[str]
    on_drag_over: NotRequired[str]
    on_drag_start: NotRequired[str]
    on_drop: NotRequired[str]
    on_duration_change: NotRequired[str]
    on_emptied: NotRequired[str]
    on_ended: NotRequired[str]
    on_error: NotRequired[str]
    on_focus: NotRequired[str]
    on_input: NotRequired[str]
    on_invalid: NotRequired[str]
    on_key_down: NotRequired[str]
    on_key_press: NotRequired[str]
    on_key_up: NotRequired[str]
    on_load: NotRequired[str]
    on_loaded_data: NotRequired[str]
    on_loaded_metadata: NotRequired[str]
    on_load_start: NotRequired[str]
    on_mouse_down: EventFunction[MouseEvent]
    on_mouse_enter: EventFunction[MouseEvent]
    on_mouse_leave: EventFunction[MouseEvent]
    on_mouse_move: EventFunction[MouseEvent]
    on_mouse_out: EventFunction[MouseEvent]
    on_mouse_over: EventFunction[MouseEvent]
    on_mouse_up: EventFunction[MouseEvent]
    on_mouse_wheel: NotRequired[str]
    on_pause: NotRequired[str]
    on_play: NotRequired[str]
    on_playing: NotRequired[str]
    on_progress: NotRequired[str]
    on_rate_change: NotRequired[str]
    on_reset: NotRequired[str]
    on_resize: NotRequired[str]
    on_scroll: NotRequired[str]
    on_seeked: NotRequired[str]
    on_seeking: NotRequired[str]
    on_select: NotRequired[str]
    on_show: NotRequired[str]
    on_sort: NotRequired[str]
    on_stalled: NotRequired[str]
    on_submit: NotRequired[str]
    on_suspend: NotRequired[str]
    on_time_update: NotRequired[str]
    on_toggle: NotRequired[str]
    on_volume_change: NotRequired[str]
    on_waiting: NotRequired[str]


class HTMLElement(TypedDict):
    access_key: NotRequired[str]
    auto_capitalize: NotRequired[str]
    class_name: NotRequired[str]
    content_editable: NotRequired[str]
    data: dict[str, str]
    dir: NotRequired[str]
    draggable: NotRequired[str]
    hidden: NotRequired[str]
    id: NotRequired[str]
    input_mode: NotRequired[str]
    lang: NotRequired[str]
    role: NotRequired[str]
    spell_check: NotRequired[str]
    style: NotRequired[str | "StyleObject"]
    tab_index: NotRequired[str]
    title: NotRequired[str]
    translate: NotRequired[str]

    init: "JS"


class HTMLAnchorElement(HTMLElement):
    download: NotRequired[str]
    href: NotRequired[str]
    href_lang: NotRequired[str]
    ping: NotRequired[str]
    referrer_policy: NotRequired[str]
    rel: NotRequired[str]
    target: NotRequired[str]
    type: NotRequired[str]


class HTMLAreaElement(HTMLElement):
    alt: NotRequired[str]
    coords: NotRequired[str]
    download: NotRequired[str]
    href: NotRequired[str]
    href_lang: NotRequired[str]
    ping: NotRequired[str]
    referrer_policy: NotRequired[str]
    rel: NotRequired[str]
    shape: NotRequired[str]
    target: NotRequired[str]


class HTMLAudioElement(HTMLElement):
    auto_play: NotRequired[str]
    controls: NotRequired[str]
    loop: NotRequired[str]
    muted: NotRequired[str]
    preload: NotRequired[str]
    src: NotRequired[str]


class HTMLBRElement(HTMLElement):
    pass  # No additional attributes


class HTMLBaseElement(HTMLElement):
    href: NotRequired[str]
    target: NotRequired[str]


class HTMLBodyElement(HTMLElement):
    background: NotRequired[str]


class HTMLButtonElement(HTMLElement):
    auto_focus: NotRequired[str]
    disabled: NotRequired[str]
    form: NotRequired[str]
    form_action: NotRequired[str]
    form_enctype: NotRequired[str]
    form_method: NotRequired[str]
    form_no_validate: NotRequired[str]
    form_target: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    value: NotRequired[str]


class HTMLCanvasElement(HTMLElement):
    height: NotRequired[str]
    width: NotRequired[str]


class HTMLDataElement(HTMLElement):
    value: NotRequired[str]


class HTMLDataListElement(HTMLElement):
    pass  # No additional attributes


class HTMLDetailsElement(HTMLElement):
    open: NotRequired[str]


class HTMLDialogElement(HTMLElement):
    open: NotRequired[str]


class HTMLDivElement(HTMLElement):
    pass  # No additional attributes


class HTMLEmbedElement(HTMLElement):
    height: NotRequired[str]
    src: NotRequired[str]
    type: NotRequired[str]
    width: NotRequired[str]


class HTMLFieldSetElement(HTMLElement):
    disabled: NotRequired[str]
    form: NotRequired[str]
    name: NotRequired[str]


class HTMLFormElement(HTMLElement):
    accept_charset: NotRequired[str]
    action: NotRequired[str]
    auto_complete: NotRequired[str]
    enctype: NotRequired[str]
    method: NotRequired[str]
    name: NotRequired[str]
    no_validate: NotRequired[str]
    target: NotRequired[str]


class HTMLHRElement(HTMLElement):
    pass  # No additional attributes


class HTMLHeadElement(HTMLElement):
    pass  # No additional attributes


class HTMLHeadingElement(HTMLElement):
    pass  # No additional attributes


class HTMLHtmlElement(HTMLElement):
    pass  # No additional attributes


class HTMLIFrameElement(HTMLElement):
    allow: NotRequired[str]
    allow_fullscreen: NotRequired[str]
    csp: NotRequired[str]
    frame_border: NotRequired[str]
    height: NotRequired[str]
    importance: NotRequired[str]
    loading: NotRequired[str]
    name: NotRequired[str]
    referrer_policy: NotRequired[str]
    sandbox: NotRequired[str]
    scrolling: NotRequired[str]
    seamless: NotRequired[str]
    src: NotRequired[str]
    srcdoc: NotRequired[str]
    width: NotRequired[str]


class HTMLImageElement(HTMLElement):
    alt: NotRequired[str]
    cross_origin: NotRequired[str]
    decoding: NotRequired[str]
    height: NotRequired[str]
    importance: NotRequired[str]
    intrinsicsize: NotRequired[str]
    ismap: NotRequired[str]
    loading: NotRequired[str]
    referrer_policy: NotRequired[str]
    sizes: NotRequired[str]
    src: NotRequired[str]
    srcset: NotRequired[str]
    usemap: NotRequired[str]
    width: NotRequired[str]


class HTMLInputElement(HTMLElement):
    accept: NotRequired[str]
    alt: NotRequired[str]
    auto_complete: NotRequired[str]
    auto_focus: NotRequired[str]
    capture: NotRequired[str]
    checked: NotRequired[str]
    cross_origin: NotRequired[str]
    disabled: NotRequired[str]
    form: NotRequired[str]
    form_action: NotRequired[str]
    form_enctype: NotRequired[str]
    form_method: NotRequired[str]
    form_no_validate: NotRequired[str]
    form_target: NotRequired[str]
    height: NotRequired[str]
    list: NotRequired[str]
    max: NotRequired[str]
    max_length: NotRequired[str]
    min: NotRequired[str]
    min_length: NotRequired[str]
    multiple: NotRequired[str]
    name: NotRequired[str]
    pattern: NotRequired[str]
    placeholder: NotRequired[str]
    readonly: NotRequired[str]
    required: NotRequired[str]
    selection_direction: NotRequired[str]
    selection_end: NotRequired[str]
    selection_start: NotRequired[str]
    size: NotRequired[str]
    src: NotRequired[str]
    step: NotRequired[str]
    type: NotRequired[str]
    value: NotRequired[str]
    width: NotRequired[str]


class HTMLListItemElement(HTMLElement):
    value: NotRequired[str]


class HTMLLabelElement(HTMLElement):
    html_for: NotRequired[str]


class HTMLLegendElement(HTMLElement):
    align: NotRequired[str]


class HTMLLinkElement(HTMLElement):
    html_as: NotRequired[str]
    cross_origin: NotRequired[str]
    disabled: NotRequired[str]
    href: NotRequired[str]
    hreflang: NotRequired[str]
    media: NotRequired[str]
    referrer_policy: NotRequired[str]
    rel: NotRequired[str]
    sizes: NotRequired[str]
    type: NotRequired[str]


class HTMLMapElement(HTMLElement):
    name: NotRequired[str]


class HTMLDocumentMetaElement(HTMLElement):
    name: NotRequired[str]
    content: NotRequired[str]


class HTMLPragmaMetaElement(HTMLElement):
    http_equiv: NotRequired[str]


class HTMLCharsetMetaElement(HTMLElement):
    charset: NotRequired[str]


class HTMLUserMetaElement(HTMLElement):
    itemprop: NotRequired[str]


class HTMLMeterElement(HTMLElement):
    form: NotRequired[str]
    high: NotRequired[str]
    low: NotRequired[str]
    max: NotRequired[str]
    min: NotRequired[str]
    optimum: NotRequired[str]
    value: NotRequired[str]


class HTMLModElement(HTMLElement):
    cite: NotRequired[str]
    datetime: NotRequired[str]


class HTMLObjectElement(HTMLElement):
    data: NotRequired[str]
    form: NotRequired[str]
    height: NotRequired[str]
    name: NotRequired[str]
    type: NotRequired[str]
    usemap: NotRequired[str]
    width: NotRequired[str]


class HTMLOrderedListElement(HTMLElement):
    reversed: NotRequired[str]
    start: NotRequired[str]


class HTMLOptGroupElement(HTMLElement):
    disabled: NotRequired[str]
    label: NotRequired[str]


class HTMLOptionElement(HTMLElement):
    disabled: NotRequired[str]
    label: NotRequired[str]
    selected: NotRequired[str]
    value: NotRequired[str]


class HTMLOutputElement(HTMLElement):
    html_for: NotRequired[str]  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: NotRequired[str]
    name: NotRequired[str]


class HTMLParagraphElement(HTMLElement):
    pass  # No additional attributes


class HTMLParamElement(HTMLElement):
    name: NotRequired[str]
    value: NotRequired[str]


class HTMLPictureElement(HTMLElement):
    pass  # No additional attributes


class HTMLPreElement(HTMLElement):
    pass  # No additional attributes


class HTMLProgressElement(HTMLElement):
    max: NotRequired[str]
    value: NotRequired[str]


class HTMLQuoteElement(HTMLElement):
    cite: NotRequired[str]


class HTMLScriptElement(HTMLElement):
    async_: NotRequired[str]  # 'async' is a reserved keyword in Python, so using 'async_'
    cross_origin: NotRequired[str]
    defer: NotRequired[str]
    integrity: NotRequired[str]
    nonce: NotRequired[str]
    referrer_policy: NotRequired[str]
    src: NotRequired[str]
    type: NotRequired[str]


class HTMLSelectElement(HTMLElement):
    auto_complete: NotRequired[str]
    auto_focus: NotRequired[str]
    disabled: NotRequired[str]
    form: NotRequired[str]
    multiple: NotRequired[str]
    name: NotRequired[str]
    required: NotRequired[str]
    size: NotRequired[str]


class HTMLSlotElement(HTMLElement):
    name: NotRequired[str]


class HTMLSourceElement(HTMLElement):
    media: NotRequired[str]
    sizes: NotRequired[str]
    src: NotRequired[str]
    srcset: NotRequired[str]
    type: NotRequired[str]


class HTMLSpanElement(HTMLElement):
    pass  # No additional attributes


class HTMLStyleElement(HTMLElement):
    media: NotRequired[str]
    nonce: NotRequired[str]
    scoped: NotRequired[str]


class HTMLTableCaptionElement(HTMLElement):
    pass  # No additional attributes


class HTMLTableCellElement(HTMLElement):
    abbr: NotRequired[str]
    colspan: NotRequired[str]
    headers: NotRequired[str]
    rowspan: NotRequired[str]
    scope: NotRequired[str]


class HTMLTableColElement(HTMLElement):
    span: NotRequired[str]


class HTMLTableDataCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableElement(HTMLElement):
    border: NotRequired[str]
    cellpadding: NotRequired[str]
    cellspacing: NotRequired[str]
    frame: NotRequired[str]
    rules: NotRequired[str]
    summary: NotRequired[str]
    width: NotRequired[str]


class HTMLTableHeaderCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableRowElement(HTMLElement):
    align: NotRequired[str]
    bgcolor: NotRequired[str]
    ch: NotRequired[str]
    choff: NotRequired[str]
    v_align: NotRequired[str]


class HTMLTableSectionElement(HTMLElement):
    align: NotRequired[str]
    ch: NotRequired[str]
    choff: NotRequired[str]
    v_align: NotRequired[str]


class HTMLTemplateElement(HTMLElement):
    pass  # No additional attributes


class HTMLTextAreaElement(HTMLElement):
    auto_complete: NotRequired[str]
    auto_focus: NotRequired[str]
    cols: NotRequired[str]
    dirname: NotRequired[str]
    disabled: NotRequired[str]
    form: NotRequired[str]
    max_length: NotRequired[str]
    min_length: NotRequired[str]
    name: NotRequired[str]
    placeholder: NotRequired[str]
    readonly: NotRequired[str]
    required: NotRequired[str]
    rows: NotRequired[str]
    wrap: NotRequired[str]


class HTMLTimeElement(HTMLElement):
    datetime: NotRequired[str]


class HTMLTitleElement(HTMLElement):
    pass  # No additional attributes


class HTMLTrackElement(HTMLElement):
    default: NotRequired[str]
    kind: NotRequired[str]
    label: NotRequired[str]
    src: NotRequired[str]
    srclang: NotRequired[str]


class HTMLUnorderedListElement(HTMLElement):
    pass  # No additional attributes


class HTMLVideoElement(HTMLElement):
    auto_play: NotRequired[str]
    controls: NotRequired[str]
    cross_origin: NotRequired[str]
    height: NotRequired[str]
    loop: NotRequired[str]
    muted: NotRequired[str]
    plays_inline: NotRequired[str]
    poster: NotRequired[str]
    preload: NotRequired[str]
    src: NotRequired[str]
    width: NotRequired[str]
