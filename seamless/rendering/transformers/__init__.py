from typing import Any, Callable

from .simple_transformer import simple_transformer as _simple_transformer
from .events_transformer import events_transformer as _events_transformer
from .class_transformer import class_transformer as _class_transformer


TRANSFORMERS = [
    _simple_transformer(),
    _events_transformer(),
]


def transformer_for(matcher: Callable[[str, Any], bool] | str):
    """
    A decorator to register a prop transformer.

    Transformers are functions that take a key, a value, and a dictionary of
    element properties.

    After handling the key and value, the transformer should update the
    element properties dictionary with the new key and value. Old keys are set to `None`
    before the transformer is called.

    Args:
        matcher: A callable that takes a key and a value and returns a boolean
        indicating whether the transformer should be applied. If a string is
        provided, it is assumed to be a key that should be matched exactly.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @transformer_for("class_name")
        ... def class_name_mapper(key, value, element_props):
        ...     if isinstance(class_name, list):
        ...         class_name = " ".join(class_name)
        ...
        ...     element_props["class"] = " ".join(str(class_name).split())

    """

    def decorator(func: Callable[[str, Any, dict[str, Any]], dict[str, Any]]):
        TRANSFORMERS.append((matcher, func))
        return func

    return decorator

transformer_for("class_name")(_class_transformer)
