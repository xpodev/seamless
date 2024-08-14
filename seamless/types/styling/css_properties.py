from typing import Any, Generic, Literal, TypeVar, TypedDict, Union, TypeAlias, NotRequired

float_ = float
T = TypeVar("T")

AlignContent: TypeAlias = Literal[
    "flex-start", "flex-end", "center", "space-between", "space-around", "stretch"
]


class StyleProperty(Generic[T]):
    def __call__(self, value: T) -> Any: ...


class CSSProperties(TypedDict):
    align_content: NotRequired[AlignContent]
    align_items: NotRequired[Literal["flex-start", "flex-end", "center", "baseline", "stretch"]]
    align_self: NotRequired[Union[
        str, Literal["auto", "flex-start", "flex-end", "center", "baseline", "stretch"]
    ]]
    animation: NotRequired[str]
    animation_delay: NotRequired[str]
    animation_direction: NotRequired[Union[
        str, Literal["normal", "reverse", "alternate", "alternate-reverse"]
    ]]
    animation_duration: NotRequired[str]
    animation_fill_mode: NotRequired[Union[str, Literal["none", "forwards", "backwards", "both"]]]
    animation_iteration_count: NotRequired[Union[str, Literal["infinite", "n"]]]
    animation_name: NotRequired[str]
    animation_play_state: NotRequired[Union[str, Literal["running", "paused"]]]
    animation_timing_function: NotRequired[str]
    backface_visibility: NotRequired[Union[str, Literal["visible", "hidden"]]]
    background: NotRequired[str]
    background_attachment: NotRequired[Union[str, Literal["scroll", "fixed", "local"]]]
    background_blend_mode: NotRequired[str]
    background_clip: NotRequired[Union[str, Literal["border-box", "padding-box", "content-box"]]]
    background_color: NotRequired[str]
    background_image: NotRequired[str]
    background_origin: NotRequired[Union[str, Literal["padding-box", "border-box", "content-box"]]]
    background_position: NotRequired[str]
    background_repeat: NotRequired[Union[
        str, Literal["repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"]
    ]]
    background_size: NotRequired[str]
    border: NotRequired[str]
    border_bottom: NotRequired[str]
    border_bottom_color: NotRequired[str]
    border_bottom_left_radius: NotRequired[str]
    border_bottom_right_radius: NotRequired[str]
    border_bottom_style: NotRequired[str]
    border_bottom_width: NotRequired[str]
    border_collapse: NotRequired[Union[str, Literal["collapse", "separate"]]]
    border_color: NotRequired[str]
    border_image: NotRequired[str]
    border_image_outset: NotRequired[str]
    border_image_repeat: NotRequired[Union[str, Literal["stretch", "repeat", "round"]]]
    border_image_slice: NotRequired[str]
    border_image_source: NotRequired[str]
    border_image_width: NotRequired[str]
    border_left: NotRequired[str]
    border_left_color: NotRequired[str]
    border_left_style: NotRequired[str]
    border_left_width: NotRequired[str]
    border_radius: NotRequired[str]
    border_right: NotRequired[str]
    border_right_color: NotRequired[str]
    border_right_style: NotRequired[str]
    border_right_width: NotRequired[str]
    border_spacing: NotRequired[str]
    border_style: NotRequired[str]
    border_top: NotRequired[str]
    border_top_color: NotRequired[str]
    border_top_left_radius: NotRequired[str]
    border_top_right_radius: NotRequired[str]
    border_top_style: NotRequired[str]
    border_top_width: NotRequired[str]
    border_width: NotRequired[str]
    bottom: NotRequired[str]
    box_shadow: NotRequired[str]
    box_sizing: NotRequired[Union[str, Literal["content-box", "border-box"]]]
    caption_side: NotRequired[Union[str, Literal["top", "bottom"]]]
    clear: NotRequired[Union[str, Literal["none", "left", "right", "both"]]]
    clip: NotRequired[str]
    color: NotRequired[str]
    column_count: NotRequired[Union[str, int]]
    column_fill: NotRequired[Union[str, Literal["balance", "auto"]]]
    column_gap: NotRequired[str]
    column_rule: NotRequired[str]
    column_rule_color: NotRequired[str]
    column_rule_style: NotRequired[str]
    column_rule_width: NotRequired[str]
    column_span: NotRequired[Union[str, Literal["none", "all"]]]
    column_width: NotRequired[Union[str, int]]
    columns: NotRequired[str]
    content: NotRequired[str]
    counter_increment: NotRequired[str]
    counter_reset: NotRequired[str]
    cursor: NotRequired[str]
    direction: NotRequired[Union[str, Literal["ltr", "rtl"]]]
    display: NotRequired[Union[
        str,
        Literal[
            "block",
            "inline",
            "inline-block",
            "flex",
            "inline-flex",
            "grid",
            "inline-grid",
            "table",
            "table-row",
            "table-cell",
            "none",
        ],
    ]]
    empty_cells: NotRequired[Union[str, Literal["show", "hide"]]]
    filter: NotRequired[str]
    flex: NotRequired[str]
    flex_basis: NotRequired[str]
    flex_direction: NotRequired[Union[str, Literal["row", "row-reverse", "column", "column-reverse"]]]
    flex_flow: NotRequired[str]
    flex_grow: NotRequired[str]
    flex_shrink: NotRequired[str]
    flex_wrap: NotRequired[Union[str, Literal["nowrap", "wrap", "wrap-reverse"]]]
    float: NotRequired[Union[str, Literal["left", "right", "none"]]]
    font: NotRequired[str]
    font_family: NotRequired[str]
    font_feature_settings: NotRequired[str]
    font_kerning: NotRequired[Union[str, Literal["auto", "normal", "none"]]]
    font_language_override: NotRequired[str]
    font_size: NotRequired[str]
    font_size_adjust: NotRequired[Union[str, Literal["none"]]]
    font_stretch: NotRequired[str]
    font_style: NotRequired[Union[str, Literal["normal", "italic", "oblique"]]]
    font_synthesis: NotRequired[str]
    font_variant: NotRequired[str]
    font_variant_alternates: NotRequired[str]
    font_variant_caps: NotRequired[Union[str, Literal["normal", "small-caps"]]]
    font_variant_east_asian: NotRequired[str]
    font_variant_ligatures: NotRequired[str]
    font_variant_numeric: NotRequired[str]
    font_variant_position: NotRequired[Union[str, Literal["normal", "sub", "super"]]]
    font_weight: NotRequired[Union[
        str,
        Literal[
            "normal",
            "bold",
            "bolder",
            "lighter",
            "100",
            "200",
            "300",
            "400",
            "500",
            "600",
            "700",
            "800",
            "900",
        ],
    ]]
    grid: NotRequired[str]
    grid_area: NotRequired[str]
    grid_auto_columns: NotRequired[str]
    grid_auto_flow: NotRequired[str]
    grid_auto_rows: NotRequired[str]
    grid_column: NotRequired[str]
    grid_column_end: NotRequired[str]
    grid_column_gap: NotRequired[str]
    grid_column_start: NotRequired[str]
    grid_gap: NotRequired[str]
    grid_row: NotRequired[str]
    grid_row_end: NotRequired[str]
    grid_row_gap: NotRequired[str]
    grid_row_start: NotRequired[str]
    grid_template: NotRequired[str]
    grid_template_areas: NotRequired[str]
    grid_template_columns: NotRequired[str]
    grid_template_rows: NotRequired[str]
    height: NotRequired[str]
    hyphens: NotRequired[Union[str, Literal["none", "manual", "auto"]]]
    image_rendering: NotRequired[str]
    isolation: NotRequired[Union[str, Literal["auto", "isolate"]]]
    justify_content: NotRequired[Union[
        str,
        Literal[
            "flex-start",
            "flex-end",
            "center",
            "space-between",
            "space-around",
            "space-evenly",
        ],
    ]]
    left: NotRequired[str]
    letter_spacing: NotRequired[str]
    line_break: NotRequired[Union[str, Literal["auto", "loose", "normal", "strict"]]]
    line_height: NotRequired[Union[str, int]]
    list_style: NotRequired[str]
    list_style_image: NotRequired[str]
    list_style_position: NotRequired[Union[str, Literal["inside", "outside"]]]
    list_style_type: NotRequired[str]
    margin: NotRequired[str]
    margin_bottom: NotRequired[str]
    margin_left: NotRequired[str]
    margin_right: NotRequired[str]
    margin_top: NotRequired[str]
    max_height: NotRequired[str]
    max_width: NotRequired[str]
    min_height: NotRequired[str]
    min_width: NotRequired[str]
    mix_blend_mode: NotRequired[str]
    object_fit: NotRequired[Union[str, Literal["fill", "contain", "cover", "none", "scale-down"]]]
    object_position: NotRequired[str]
    opacity: NotRequired[Union[str, float_]]
    order: NotRequired[Union[str, int]]
    outline: NotRequired[str]
    outline_color: NotRequired[str]
    outline_offset: NotRequired[str]
    outline_style: NotRequired[str]
    outline_width: NotRequired[str]
    overflow: NotRequired[Union[str, Literal["auto", "hidden", "scroll", "visible"]]]
    overflow_wrap: NotRequired[Union[str, Literal["normal", "break-word", "anywhere"]]]
    overflow_x: NotRequired[Union[str, Literal["auto", "hidden", "scroll", "visible"]]]
    overflow_y: NotRequired[Union[str, Literal["auto", "hidden", "scroll", "visible"]]]
    padding: NotRequired[str]
    padding_bottom: NotRequired[str]
    padding_left: NotRequired[str]
    padding_right: NotRequired[str]
    padding_top: NotRequired[str]
    page_break_after: NotRequired[Union[str, Literal["auto", "always", "avoid", "left", "right"]]]
    page_break_before: NotRequired[Union[str, Literal["auto", "always", "avoid", "left", "right"]]]
    page_break_inside: NotRequired[Union[str, Literal["auto", "avoid"]]]
    perspective: NotRequired[str]
    perspective_origin: NotRequired[str]
    position: NotRequired[Union[str, Literal["static", "relative", "absolute", "fixed", "sticky"]]]
    quotes: NotRequired[str]
    resize: NotRequired[Union[str, Literal["none", "both", "horizontal", "vertical"]]]
    right: NotRequired[str]
    scroll_behavior: NotRequired[Union[str, Literal["auto", "smooth"]]]
    tab_size: NotRequired[Union[str, int]]
    table_layout: NotRequired[Union[str, Literal["auto", "fixed"]]]
    text_align: NotRequired[Union[str, Literal["left", "right", "center", "justify", "start", "end"]]]
    text_align_last: NotRequired[Union[str, Literal["auto", "left", "right", "center", "justify", "start", "end"]]]
    text_decoration: NotRequired[str]
    text_decoration_color: NotRequired[str]
    text_decoration_line: NotRequired[str]
    text_decoration_style: NotRequired[str]
    text_indent: NotRequired[str]
    text_justify: NotRequired[Union[str, Literal["auto", "inter-word", "inter-character", "none"]]]
    text_overflow: NotRequired[Union[str, Literal["clip", "ellipsis"]]]
    text_shadow: NotRequired[str]
    text_transform: NotRequired[Union[str, Literal["none", "capitalize", "uppercase", "lowercase", "full-width"]]]
    text_underline_position: NotRequired[str]
    top: NotRequired[str]
    transform: NotRequired[str]
    transform_origin: NotRequired[str]
    transform_style: NotRequired[Union[str, Literal["flat", "preserve-3d"]]]
    transition: NotRequired[str]
    transition_delay: NotRequired[str]
    transition_duration: NotRequired[str]
    transition_property: NotRequired[str]
    transition_timing_function: NotRequired[str]
    unicode_bidi: NotRequired[Union[str, Literal["normal", "embed", "isolate", "bidi-override"]]]
    user_select: NotRequired[Union[str, Literal["auto", "text", "none", "contain", "all"]]]
    vertical_align: NotRequired[str]
    visibility: NotRequired[Union[str, Literal["visible", "hidden", "collapse"]]]
    white_space: NotRequired[Union[str, Literal["normal", "nowrap", "pre", "pre-line", "pre-wrap"]]]
    widows: NotRequired[Union[str, int]]
    width: NotRequired[str]
    will_change: NotRequired[str]
    word_break: NotRequired[Union[str, Literal["normal", "break-all", "keep-all", "break-word"]]]
    word_spacing: NotRequired[str]
    writing_mode: NotRequired[Union[
        str,
        Literal[
            "horizontal-tb", "vertical-rl", "vertical-lr", "sideways-rl", "sideways-lr"
        ],
    ]]
    z_index: NotRequired[Union[str, int]]
