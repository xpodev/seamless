from ...core import JavaScript
from ...internal.constants import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE


def init_transformer():
    def matcher(key: str, value):
        return key == "init" and isinstance(value, JavaScript)

    def transformer(key: str, source: JavaScript, element):
        element.props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        element.props[SEAMLESS_INIT_ATTRIBUTE] = (
            element.props.get(SEAMLESS_INIT_ATTRIBUTE, "") + source.code
        )
        del element.props[key]

    return matcher, transformer


def js_transformer():
    def matcher(key: str, value):
        return key.startswith("on_") and isinstance(value, JavaScript)

    def transformer(key: str, source: JavaScript, element):
        event_name = key.removeprefix("on_")

        element.props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        element.props[SEAMLESS_INIT_ATTRIBUTE] = (
            element.props.get(SEAMLESS_INIT_ATTRIBUTE, "")
            + f"\nthis.addEventListener('{event_name}', (event) => {{{source.code}}});"
        )
        del element.props[key]

    return matcher, transformer
