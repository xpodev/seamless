import os
from typing import (
    Any,
    Callable,
    Concatenate,
    Optional,
    ParamSpec,
    TypeVar,
    cast,
)

from pydom.context.context import (
    Context as _Context,
    get_context as _get_context,
    set_default_context as _set_global_context,
)
from pydom.rendering.tree.nodes import ContextNode

from ..errors import Error
from ..internal.constants import DISABLE_GLOBAL_CONTEXT_ENV
from ..internal.injector import Injector

T = TypeVar("T", bound=_Context)
P = ParamSpec("P")

Feature = Callable[Concatenate["Context", P], Any]
PropertyMatcher = Callable[Concatenate[str, Any, P], bool] | str
PropertyTransformer = Callable[Concatenate[str, Any, "ContextNode", P], None]
PostRenderTransformer = Callable[Concatenate["ContextNode", P], None]


class Context(_Context):
    def __init__(self) -> None:
        super().__init__()
        self.injector = Injector()
        self.injector.add(Context, self)

    @classmethod
    def standard(cls) -> "Context":
        context = cls()

        from .default import add_standard_features

        add_standard_features(context)
        return context


def get_context(context: Optional[Context] = None):
    if context is None:
        context = cast(Optional[Context], _get_context())

    if context is None:
        if os.getenv(DISABLE_GLOBAL_CONTEXT_ENV):
            raise Error(
                f"Global context is disabled by {DISABLE_GLOBAL_CONTEXT_ENV} environment variable. "
                "You must provide a context explicitly. Did you forget to call set_global_context?"
            ) from None

        raise Error(
            "No global context found. Did you forget to call set_global_context?"
        )

    return context


def set_global_context(context: _Context):
    _set_global_context(context)
