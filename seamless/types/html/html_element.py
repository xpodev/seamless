from typing import TYPE_CHECKING, Iterable, Union

from typing_extensions import TypedDict

if TYPE_CHECKING:
    from seamless.core.javascript import JS
    from seamless.styling import StyleObject


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
