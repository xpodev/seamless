from ...core import JavaScript
from ...internal.constants import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE


def init_transformer():
    def matcher(key: str, value):
        return key == "init" and isinstance(value, JavaScript)

    def transformer(key: str, source: JavaScript, props):
        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        props[SEAMLESS_INIT_ATTRIBUTE] = (
            props.get(SEAMLESS_INIT_ATTRIBUTE, "") + source.code
        )
        del props[key]

    return matcher, transformer


def js_transformer():
    def matcher(key: str, value):
        return key.startswith("on_") and isinstance(value, JavaScript)

    def transformer(key: str, source: JavaScript, props):
        event_name = key.removeprefix("on_")

        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        props[SEAMLESS_INIT_ATTRIBUTE] = (
            props.get(SEAMLESS_INIT_ATTRIBUTE, "")
            + f"\nthis.addEventListener('{event_name}', (event) => {{{source.code}}});"
        )
        del props[key]

    return matcher, transformer
