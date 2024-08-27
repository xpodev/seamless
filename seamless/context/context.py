from typing import Callable, Concatenate, ParamSpec, Any, TYPE_CHECKING, TypeVar, overload
from socketio import AsyncServer

from .base import ContextBase

from ..errors import ClientError

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


class Context(ContextBase):
    def __init__(self) -> None:
        super().__init__()
        self.server = AsyncServer(async_mode="asgi")
        self.injector.add(Context, self)

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

    @classmethod
    def standard(cls) -> "Context":
        context = cls()

        from .default import add_standard_features

        add_standard_features(context)
        return context


_GLOBAL_CONTEXT: ContextBase = Context.standard()

CT = TypeVar("CT", bound=ContextBase)

@overload
def get_context(context: None = None) -> Context: ...
@overload
def get_context(context: CT) -> CT: ...

def get_context(context: ContextBase | None = None):
    return context or _GLOBAL_CONTEXT


def set_global_context(context: ContextBase):
    global _GLOBAL_CONTEXT
    _GLOBAL_CONTEXT = context
