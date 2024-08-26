from typing import Callable, Concatenate, ParamSpec, Any, TYPE_CHECKING, TypeVar
from socketio import AsyncServer

from ..errors import ClientError

from ..internal.injector import Injector
from ..internal.utils import to_async, wraps

from .request import WSRequest, set_request

if TYPE_CHECKING:
    from ..rendering.tree import ElementNode

T = TypeVar("T")

P = ParamSpec("P")
Feature = Callable[Concatenate["Context", P], Any]

PropertyMatcher = Callable[Concatenate[str, Any, ...], bool] | str
PropertyTransformer = Callable[Concatenate[str, Any, "ElementNode", ...], None]
PostRenderTransformer = Callable[Concatenate["ElementNode", ...], None]

class Context:
    def __init__(self) -> None:
        self.server = AsyncServer(async_mode="asgi")
        self.injector = Injector()
        self.injector.add(Context, self)
        self._prop_transformers: list[tuple[PropertyMatcher, PropertyTransformer]] = []
        self._post_render_transformers: list[PostRenderTransformer] = []
        self._features: dict[type, Any] = {}

    def on(self, event, handler):
        @wraps(handler)
        async def wrapper(sid, *args, **kwargs):
            try:
                WSRequest.make(sid)
                result = await to_async(handler)(sid, *args, **kwargs)
                set_request(None)
                return result
            except ClientError as e:
                await self.server.emit("error", str(e), to=sid)
            except Exception as e:
                await self.server.emit("error", str(e), to=sid)
                raise e

        self.server.on(event, wrapper)

    async def emit(self, event: str, *args):
        return await self.server.emit(event, *args)

    def add_feature(self, feature: Feature[P], *args: P.args, **kwargs: P.kwargs):
            result = feature(self, *args, **kwargs)
            if isinstance(feature, type):
                self._features[feature] = result

    def get_feature(self, feature: type[T]) -> T:
        return self._features[feature]

    def add_prop_transformer(
        self,
        matcher: PropertyMatcher,
        transformer: PropertyTransformer
    ):
        self._prop_transformers.append((matcher, self.inject(transformer)))

    def add_post_render_transformer(
        self, transformer: PostRenderTransformer
    ):
        self._post_render_transformers.append(self.inject(transformer))

    @property
    def prop_transformers(self):
        return self._prop_transformers
    
    @property
    def post_render_transformers(self):
        return self._post_render_transformers

    @classmethod
    def standard(cls) -> "Context":
        context = cls()

        from .default import add_standard_features

        add_standard_features(context)
        return context

    def inject(self, callback: Callable) -> Callable:
        return self.injector.inject(callback)


_GLOBAL_CONTEXT = Context.standard()


def get_context(context: Context | None = None) -> Context:
    return context or _GLOBAL_CONTEXT


def set_global_context(context: Context):
    global _GLOBAL_CONTEXT
    _GLOBAL_CONTEXT = context