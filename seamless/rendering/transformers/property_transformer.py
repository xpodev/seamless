from typing import Any, Callable
from ...context.context import PropertyTransformer, Context, get_context


def property_transformer(
    matcher: Callable[[str, Any], bool] | str, context: Context | None = None
):
    """
    A decorator to register a property transformer.

    Transformers are functions that take a key, a value, and the element node object.

    After handling the key and value, the transformer should update the element node
    properties in place.

    Args:
        matcher: A callable that takes a key and a value and returns a boolean
        indicating whether the transformer should be applied.
        If a string is provided, it is assumed to be a key that should be matched exactly.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @property_transformer("class_name")
        ... def class_name_mapper(key, value, element):
        ...     if isinstance(class_name, list):
        ...         class_name = " ".join(class_name)
        ...
        ...     element.props["class"] = " ".join(str(class_name).split())

    """
    context = get_context(context)

    def decorator(func: PropertyTransformer):
        context.add_prop_transformer(matcher, func)
        return func

    return decorator
