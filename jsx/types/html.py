from typing import TypedDict, Callable, TypeVar
from .events import Event, MouseEvent

EventProps = TypeVar("EventProps", bound=Event)
EventFunction = Callable[[EventProps], None]


class AriaProps(TypedDict):
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


class HTMLEventProps(TypedDict):
    on_abort: str
    on_auto_complete: str
    on_auto_complete_error: str
    on_blur: str
    on_cancel: str
    on_can_play: str
    on_can_play_through: str
    on_change: str
    on_click: EventFunction[MouseEvent]
    on_close: str
    on_context_menu: EventFunction[MouseEvent]
    on_cue_change: str
    on_dbl_click: EventFunction[MouseEvent]
    on_drag: str
    on_drag_end: str
    on_drag_enter: str
    on_drag_leave: str
    on_drag_over: str
    on_drag_start: str
    on_drop: str
    on_duration_change: str
    on_emptied: str
    on_ended: str
    on_error: str
    on_focus: str
    on_input: str
    on_invalid: str
    on_key_down: str
    on_key_press: str
    on_key_up: str
    on_load: str
    on_loaded_data: str
    on_loaded_metadata: str
    on_load_start: str
    on_mouse_down: EventFunction[MouseEvent]
    on_mouse_enter: EventFunction[MouseEvent]
    on_mouse_leave: EventFunction[MouseEvent]
    on_mouse_move: EventFunction[MouseEvent]
    on_mouse_out: EventFunction[MouseEvent]
    on_mouse_over: EventFunction[MouseEvent]
    on_mouse_up: EventFunction[MouseEvent]
    on_mouse_wheel: str
    on_pause: str
    on_play: str
    on_playing: str
    on_progress: str
    on_rate_change: str
    on_reset: str
    on_resize: str
    on_scroll: str
    on_seeked: str
    on_seeking: str
    on_select: str
    on_show: str
    on_sort: str
    on_stalled: str
    on_submit: str
    on_suspend: str
    on_time_update: str
    on_toggle: str
    on_volume_change: str
    on_waiting: str


class HTMLElement(TypedDict):
    access_key: str
    auto_capitalize: str
    class_name: str
    content_editable: str
    data: dict[str, str]
    dir: str
    draggable: str
    hidden: str
    id: str
    input_mode: str
    lang: str
    role: str
    spell_check: str
    style: str
    tab_index: str
    title: str
    translate: str


class HTMLAnchorElement(HTMLElement):
    download: str
    href: str
    href_lang: str
    ping: str
    referrer_policy: str
    rel: str
    target: str
    type: str


class HTMLAreaElement(HTMLElement):
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


class HTMLAudioElement(HTMLElement):
    auto_play: str
    controls: str
    loop: str
    muted: str
    preload: str
    src: str


class HTMLBRElement(HTMLElement):
    pass  # No additional attributes


class HTMLBaseElement(HTMLElement):
    href: str
    target: str


class HTMLBodyElement(HTMLElement):
    background: str


class HTMLButtonElement(HTMLElement):
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


class HTMLCanvasElement(HTMLElement):
    height: str
    width: str


class HTMLDataElement(HTMLElement):
    value: str


class HTMLDataListElement(HTMLElement):
    pass  # No additional attributes


class HTMLDetailsElement(HTMLElement):
    open: str


class HTMLDialogElement(HTMLElement):
    open: str


class HTMLDivElement(HTMLElement):
    pass  # No additional attributes


class HTMLEmbedElement(HTMLElement):
    height: str
    src: str
    type: str
    width: str


class HTMLFieldSetElement(HTMLElement):
    disabled: str
    form: str
    name: str


class HTMLFormElement(HTMLElement):
    accept_charset: str
    action: str
    auto_complete: str
    enctype: str
    method: str
    name: str
    no_validate: str
    target: str


class HTMLHRElement(HTMLElement):
    pass  # No additional attributes


class HTMLHeadElement(HTMLElement):
    pass  # No additional attributes


class HTMLHeadingElement(HTMLElement):
    pass  # No additional attributes


class HTMLHtmlElement(HTMLElement):
    pass  # No additional attributes


class HTMLIFrameElement(HTMLElement):
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


class HTMLImageElement(HTMLElement):
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


class HTMLInputElement(HTMLElement):
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


class HTMLListItemElement(HTMLElement):
    value: str


class HTMLLabelElement(HTMLElement):
    html_for: str


class HTMLLegendElement(HTMLElement):
    align: str


class HTMLLinkElement(HTMLElement):
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


class HTMLMapElement(HTMLElement):
    name: str


class HTMLDocumentMetaElement(HTMLElement):
    name: str
    content: str


class HTMLPragmaMetaElement(HTMLElement):
    http_equiv: str


class HTMLCharsetMetaElement(HTMLElement):
    charset: str


class HTMLUserMetaElement(HTMLElement):
    itemprop: str


class HTMLMeterElement(HTMLElement):
    form: str
    high: str
    low: str
    max: str
    min: str
    optimum: str
    value: str


class HTMLModElement(HTMLElement):
    cite: str
    datetime: str


class HTMLObjectElement(HTMLElement):
    data: str
    form: str
    height: str
    name: str
    type: str
    usemap: str
    width: str


class HTMLOrderedListElement(HTMLElement):
    reversed: str
    start: str


class HTMLOptGroupElement(HTMLElement):
    disabled: str
    label: str


class HTMLOptionElement(HTMLElement):
    disabled: str
    label: str
    selected: str
    value: str


class HTMLOutputElement(HTMLElement):
    html_for: str  # 'for' is a reserved keyword in Python, so using 'html_for'
    form: str
    name: str


class HTMLParagraphElement(HTMLElement):
    pass  # No additional attributes


class HTMLParamElement(HTMLElement):
    name: str
    value: str


class HTMLPictureElement(HTMLElement):
    pass  # No additional attributes


class HTMLPreElement(HTMLElement):
    pass  # No additional attributes


class HTMLProgressElement(HTMLElement):
    max: str
    value: str


class HTMLQuoteElement(HTMLElement):
    cite: str


class HTMLScriptElement(HTMLElement):
    async_: str  # 'async' is a reserved keyword in Python, so using 'async_'
    cross_origin: str
    defer: str
    integrity: str
    nonce: str
    referrer_policy: str
    src: str
    type: str


class HTMLSelectElement(HTMLElement):
    auto_complete: str
    auto_focus: str
    disabled: str
    form: str
    multiple: str
    name: str
    required: str
    size: str


class HTMLSlotElement(HTMLElement):
    name: str


class HTMLSourceElement(HTMLElement):
    media: str
    sizes: str
    src: str
    srcset: str
    type: str


class HTMLSpanElement(HTMLElement):
    pass  # No additional attributes


class HTMLStyleElement(HTMLElement):
    media: str
    nonce: str
    scoped: str


class HTMLTableCaptionElement(HTMLElement):
    pass  # No additional attributes


class HTMLTableCellElement(HTMLElement):
    abbr: str
    colspan: str
    headers: str
    rowspan: str
    scope: str


class HTMLTableColElement(HTMLElement):
    span: str


class HTMLTableDataCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableElement(HTMLElement):
    border: str
    cellpadding: str
    cellspacing: str
    frame: str
    rules: str
    summary: str
    width: str


class HTMLTableHeaderCellElement(HTMLTableCellElement):
    pass  # Inherits attributes from HTMLTableCellElement


class HTMLTableRowElement(HTMLElement):
    align: str
    bgcolor: str
    ch: str
    choff: str
    v_align: str


class HTMLTableSectionElement(HTMLElement):
    align: str
    ch: str
    choff: str
    v_align: str


class HTMLTemplateElement(HTMLElement):
    pass  # No additional attributes


class HTMLTextAreaElement(HTMLElement):
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


class HTMLTimeElement(HTMLElement):
    datetime: str


class HTMLTitleElement(HTMLElement):
    pass  # No additional attributes


class HTMLTrackElement(HTMLElement):
    default: str
    kind: str
    label: str
    src: str
    srclang: str


class HTMLUnorderedListElement(HTMLElement):
    pass  # No additional attributes


class HTMLVideoElement(HTMLElement):
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
