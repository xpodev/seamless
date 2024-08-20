from typing import Any, Callable, TYPE_CHECKING

from ...context.context import PostRenderTransformer, PropertyTransformer

if TYPE_CHECKING:
    from ...context.context import Context

def property_transformer(matcher: Callable[[str, Any], bool] | str, context: "Context | None" = None):
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
    from ...context.context import get_context
    context = get_context(context)

    def decorator(func: PropertyTransformer):
        context.add_prop_transformer(matcher, func)
        return func

    return decorator


def post_render_transformer(context: "Context | None" = None):
    """
    A decorator to register a post-render transformer.

    Post-render transformers are functions that take the rendered tree and can modify it in place.

    Args:
        context: The context to register the transformer with.

    Returns:
        A decorator that takes a transformer function and registers it.

    Example:
        >>> @post_render_transformer()
        ... def add_custom_script(root: TreeNode) -> TreeNode:
        ...     root.get_by_tag("head").append_child(
        ...         ElementNode(
        ...             tag_name="script",
        ...             props={"src": "/custom.js"},
        ...         )
        ...     )

    """
    from ...context.context import get_context
    context = get_context(context)

    def decorator(func: PostRenderTransformer):
        context.add_post_render_transformer(func)
        return func

    return decorator