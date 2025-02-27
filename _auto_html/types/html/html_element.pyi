from typing import TYPE_CHECKING, Dict, Iterable, Union, Literal, Optional

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from pydom.styling import StyleSheet


class HTMLElement(TypedDict, total=False, closed=False):
    access_key: Optional[str]
    auto_capitalize: Optional[str]
    classes: Optional[Union[str, Iterable[str]]]
    content_editable: Optional[str]
    dangerously_set_inner_html: Optional[Dict[Literal["__html"], str]]
    # data: Dict[str, str]  # add this if needed in the future
    dir: Optional[Literal["ltr", "rtl", "auto"]]
    draggable: Optional[str]
    hidden: Optional[str]
    id: Optional[str]
    input_mode: Optional[str]
    lang: Optional[str]
    role: Optional[str]
    spell_check: Optional[str]
    style: Optional[Union[str, "StyleSheet"]]
    tab_index: Optional[str]
    title: Optional[str]
    translate: Optional[str]
