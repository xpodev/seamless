from typing import Callable, Concatenate, ParamSpec, Any
from socketio import AsyncServer

from ..errors import ClientError

from ..internal.utils import to_async, wraps

from .request import WSRequest, set_request

P = ParamSpec("P")
Feature = Callable[Concatenate["Context", P], Any]


class Context:
    def __init__(self) -> None:
        """
        :param claim_time: The time in seconds that a claim for an element is valid
        """
        self.server = AsyncServer(async_mode="asgi")
        self._prop_transformers = []
        self._post_dict_render_transformers = []

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
        feature(self, *args, **kwargs)

    def add_prop_transformer(
        self,
        matcher: Callable[[str, Any], bool] | str,
        transformer: Callable[[str, Any, dict[str, Any]], None],
    ):
        self._prop_transformers.append((matcher, transformer))

    def add_post_dict_render_transformer(
        self, transformer: Callable[[dict[str, Any]], dict[str, Any]]
    ):
        self._post_dict_render_transformers.append(transformer)

    @classmethod
    def standard(cls) -> "Context":
        context = cls()

        from .default import add_standard_features

        add_standard_features(context)
        return context


_DEFAULT_CONTEXT = Context.standard()


def get_context(context: Context | None = None) -> Context:
    return context or _DEFAULT_CONTEXT
