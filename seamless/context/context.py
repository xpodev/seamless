import os
from typing import (
    Any,
    Callable,
    Dict,
    Optional,
    Type,
    TypeVar,
    cast,
)

from typing_extensions import Concatenate, ParamSpec
from pydom.context.context import (
    Context as _Context,
    get_context as _get_context,
    set_default_context as _set_global_context,
)

from ..errors import Error
from .feature import Feature
from ..internal.constants import DISABLE_GLOBAL_CONTEXT_ENV

_P = ParamSpec("_P")
_T = TypeVar("_T", bound=Feature)

FeatureFactory = Callable[Concatenate["Context", _P], Feature]


class Context(_Context):
    def __init__(self) -> None:
        super().__init__()
        self._features: Dict[Type[Feature], Feature] = {}

    def add_feature(self, feature: FeatureFactory[_P], *args: _P.args, **kwargs: _P.kwargs):
        result = feature(self, *args, **kwargs)
        if isinstance(feature, type):
            self._features[feature] = result

    def get_feature(self, feature_type: Type[_T]) -> _T:
        try:
            return cast(_T, self._features[feature_type])
        except KeyError:
            for instance in self._features.values():
                if isinstance(instance, feature_type):
                    return instance

            raise

    @classmethod
    def standard(cls: Type["Context"]) -> "Context":
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

        raise Error("No global context found. Did you forget to call set_global_context?")

    return context


def set_global_context(context: Context):
    _set_global_context(context)
