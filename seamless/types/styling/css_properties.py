from typing import Any, Generic, Literal, TypeVar, TypedDict, Union, TypeAlias

float_ = float
T = TypeVar("T")

AlignContent: TypeAlias = Literal[
    "flex-start", "flex-end", "center", "space-between", "space-around", "stretch"
]


class StyleProperty(Generic[T]):
    def __call__(self, value: T) -> Any: ...


class CSSProperties(TypedDict):
    align_content: AlignContent
    align_items: Literal["flex-start", "flex-end", "center", "baseline", "stretch"]
    align_self: Union[
        str, Literal["auto", "flex-start", "flex-end", "center", "baseline", "stretch"]
    ]
    animation: str
    animation_delay: str
    animation_direction: Union[
        str, Literal["normal", "reverse", "alternate", "alternate-reverse"]
    ]
    animation_duration: str
    animation_fill_mode: Union[str, Literal["none", "forwards", "backwards", "both"]]
    animation_iteration_count: Union[str, Literal["infinite", "n"]]
    animation_name: str
    animation_play_state: Union[str, Literal["running", "paused"]]
    animation_timing_function: str
    backface_visibility: Union[str, Literal["visible", "hidden"]]
    background: str
    background_attachment: Union[str, Literal["scroll", "fixed", "local"]]
    background_blend_mode: str
    background_clip: Union[str, Literal["border-box", "padding-box", "content-box"]]
    background_color: str
    background_image: str
    background_origin: Union[str, Literal["padding-box", "border-box", "content-box"]]
    background_position: str
    background_repeat: Union[
        str, Literal["repeat", "repeat-x", "repeat-y", "no-repeat", "space", "round"]
    ]
    background_size: str
    border: str
    border_bottom: str
    border_bottom_color: str
    border_bottom_left_radius: str
    border_bottom_right_radius: str
    border_bottom_style: str
    border_bottom_width: str
    border_collapse: Union[str, Literal["collapse", "separate"]]
    border_color: str
    border_image: str
    border_image_outset: str
    border_image_repeat: Union[str, Literal["stretch", "repeat", "round"]]
    border_image_slice: str
    border_image_source: str
    border_image_width: str
    border_left: str
    border_left_color: str
    border_left_style: str
    border_left_width: str
    border_radius: str
    border_right: str
    border_right_color: str
    border_right_style: str
    border_right_width: str
    border_spacing: str
    border_style: str
    border_top: str
    border_top_color: str
    border_top_left_radius: str
    border_top_right_radius: str
    border_top_style: str
    border_top_width: str
    border_width: str
    bottom: str
    box_shadow: str
    box_sizing: Union[str, Literal["content-box", "border-box"]]
    caption_side: Union[str, Literal["top", "bottom"]]
    clear: Union[str, Literal["none", "left", "right", "both"]]
    clip: str
    color: str
    column_count: Union[str, int]
    column_fill: Union[str, Literal["balance", "auto"]]
    column_gap: str
    column_rule: str
    column_rule_color: str
    column_rule_style: str
    column_rule_width: str
    column_span: Union[str, Literal["none", "all"]]
    column_width: Union[str, int]
    columns: str
    content: str
    counter_increment: str
    counter_reset: str
    cursor: str
    direction: Union[str, Literal["ltr", "rtl"]]
    display: Union[
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
    ]
    empty_cells: Union[str, Literal["show", "hide"]]
    filter: str
    flex: str
    flex_basis: str
    flex_direction: Union[
        str, Literal["row", "row-reverse", "column", "column-reverse"]
    ]
    flex_flow: str
    flex_grow: str
    flex_shrink: str
    flex_wrap: Union[str, Literal["nowrap", "wrap", "wrap-reverse"]]
    float: Union[str, Literal["left", "right", "none"]]
    font: str
    font_family: str
    font_feature_settings: str
    font_kerning: Union[str, Literal["auto", "normal", "none"]]
    font_language_override: str
    font_size: str
    font_size_adjust: Union[str, Literal["none"]]
    font_stretch: str
    font_style: Union[str, Literal["normal", "italic", "oblique"]]
    font_synthesis: str
    font_variant: str
    font_variant_alternates: str
    font_variant_caps: Union[str, Literal["normal", "small-caps"]]
    font_variant_east_asian: str
    font_variant_ligatures: str
    font_variant_numeric: str
    font_variant_position: Union[str, Literal["normal", "sub", "super"]]
    font_weight: Union[
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
    ]
    grid: str
    grid_area: str
    grid_auto_columns: str
    grid_auto_flow: str
    grid_auto_rows: str
    grid_column: str
    grid_column_end: str
    grid_column_gap: str
    grid_column_start: str
    grid_gap: str
    grid_row: str
    grid_row_end: str
    grid_row_gap: str
    grid_row_start: str
    grid_template: str
    grid_template_areas: str
    grid_template_columns: str
    grid_template_rows: str
    height: str
    hyphens: Union[str, Literal["none", "manual", "auto"]]
    image_rendering: str
    isolation: Union[str, Literal["auto", "isolate"]]
    justify_content: Union[
        str,
        Literal[
            "flex-start",
            "flex-end",
            "center",
            "space-between",
            "space-around",
            "space-evenly",
        ],
    ]
    left: str
    letter_spacing: str
    line_break: Union[str, Literal["auto", "loose", "normal", "strict"]]
    line_height: Union[str, int]
    list_style: str
    list_style_image: str
    list_style_position: Union[str, Literal["inside", "outside"]]
    list_style_type: str
    margin: str
    margin_bottom: str
    margin_left: str
    margin_right: str
    margin_top: str
    max_height: str
    max_width: str
    min_height: str
    min_width: str
    mix_blend_mode: str
    object_fit: Union[str, Literal["fill", "contain", "cover", "none", "scale-down"]]
    object_position: str
    opacity: Union[str, float_]
    order: Union[str, int]
    outline: str
    outline_color: str
    outline_offset: str
    outline_style: str
    outline_width: str
    overflow: Union[str, Literal["auto", "hidden", "scroll", "visible"]]
    overflow_wrap: Union[str, Literal["normal", "break-word", "anywhere"]]
    overflow_x: Union[str, Literal["auto", "hidden", "scroll", "visible"]]
    overflow_y: Union[str, Literal["auto", "hidden", "scroll", "visible"]]
    padding: str
    padding_bottom: str
    padding_left: str
    padding_right: str
    padding_top: str
    page_break_after: Union[str, Literal["auto", "always", "avoid", "left", "right"]]
    page_break_before: Union[str, Literal["auto", "always", "avoid", "left", "right"]]
    page_break_inside: Union[str, Literal["auto", "avoid"]]
    perspective: str
    perspective_origin: str
    position: Union[str, Literal["static", "relative", "absolute", "fixed", "sticky"]]
    quotes: str
    resize: Union[str, Literal["none", "both", "horizontal", "vertical"]]
    right: str
    scroll_behavior: Union[str, Literal["auto", "smooth"]]
    tab_size: Union[str, int]
    table_layout: Union[str, Literal["auto", "fixed"]]
    text_align: Union[
        str, Literal["left", "right", "center", "justify", "start", "end"]
    ]
    text_align_last: Union[
        str, Literal["auto", "left", "right", "center", "justify", "start", "end"]
    ]
    text_decoration: str
    text_decoration_color: str
    text_decoration_line: str
    text_decoration_style: str
    text_indent: str
    text_justify: Union[str, Literal["auto", "inter-word", "inter-character", "none"]]
    text_overflow: Union[str, Literal["clip", "ellipsis"]]
    text_shadow: str
    text_transform: Union[
        str, Literal["none", "capitalize", "uppercase", "lowercase", "full-width"]
    ]
    text_underline_position: str
    top: str
    transform: str
    transform_origin: str
    transform_style: Union[str, Literal["flat", "preserve-3d"]]
    transition: str
    transition_delay: str
    transition_duration: str
    transition_property: str
    transition_timing_function: str
    unicode_bidi: Union[str, Literal["normal", "embed", "isolate", "bidi-override"]]
    user_select: Union[str, Literal["auto", "text", "none", "contain", "all"]]
    vertical_align: str
    visibility: Union[str, Literal["visible", "hidden", "collapse"]]
    white_space: Union[str, Literal["normal", "nowrap", "pre", "pre-line", "pre-wrap"]]
    widows: Union[str, int]
    width: str
    will_change: str
    word_break: Union[str, Literal["normal", "break-all", "keep-all", "break-word"]]
    word_spacing: str
    writing_mode: Union[
        str,
        Literal[
            "horizontal-tb", "vertical-rl", "vertical-lr", "sideways-rl", "sideways-lr"
        ],
    ]
    z_index: Union[str, int]


# class CSSProperties2:
#     align_content: StyleProperty[AlignContent]
#     align_items: StyleProperty[Union[str, CSSProperties.align_items]]
#     align_self: StyleProperty[Union[str, CSSProperties.align_self]]
#     animation: StyleProperty[str]
#     animation_delay: StyleProperty[str]
#     animation_direction: StyleProperty[Union[str, CSSProperties.animation_direction]]
#     animation_duration: StyleProperty[str]
#     animation_fill_mode: StyleProperty[Union[str, CSSProperties.animation_fill_mode]]
#     animation_iteration_count: StyleProperty[
#         Union[str, CSSProperties.animation_iteration_count]
#     ]
#     animation_name: StyleProperty[str]
#     animation_play_state: StyleProperty[Union[str, CSSProperties.animation_play_state]]
#     animation_timing_function: StyleProperty[str]
#     backface_visibility: StyleProperty[Union[str, CSSProperties.backface_visibility]]
#     background: StyleProperty[str]
#     background_attachment: StyleProperty[
#         Union[str, CSSProperties.background_attachment]
#     ]
#     background_blend_mode: StyleProperty[str]
#     background_clip: StyleProperty[Union[str, CSSProperties.background_clip]]
#     background_color: StyleProperty[str]
#     background_image: StyleProperty[str]
#     background_origin: StyleProperty[Union[str, CSSProperties.background_origin]]
#     background_position: StyleProperty[str]
#     background_repeat: StyleProperty[Union[str, CSSProperties.background_repeat]]
#     background_size: StyleProperty[str]
#     border: StyleProperty[str]
#     border_bottom: StyleProperty[str]
#     border_bottom_color: StyleProperty[str]
#     border_bottom_left_radius: StyleProperty[str]
#     border_bottom_right_radius: StyleProperty[str]
#     border_bottom_style: StyleProperty[str]
#     border_bottom_width: StyleProperty[str]
#     border_collapse: StyleProperty[Union[str, CSSProperties.border_collapse]]
#     border_color: StyleProperty[str]
#     border_image: StyleProperty[str]
#     border_image_outset: StyleProperty[str]
#     border_image_repeat: StyleProperty[Union[str, CSSProperties.border_image_repeat]]
#     border_image_slice: StyleProperty[str]
#     border_image_source: StyleProperty[str]
#     border_image_width: StyleProperty[str]
#     border_left: StyleProperty[str]
#     border_left_color: StyleProperty[str]
#     border_left_style: StyleProperty[str]
#     border_left_width: StyleProperty[str]
#     border_radius: StyleProperty[str]
#     border_right: StyleProperty[str]
#     border_right_color: StyleProperty[str]
#     border_right_style: StyleProperty[str]
