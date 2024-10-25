from typing import Any, Callable, Generic, TYPE_CHECKING, TypeVar, Awaitable

from pydom import Context
from typing_extensions import ParamSpec


if TYPE_CHECKING:
    from .transport import TransportFeature

_P = ParamSpec("_P")
_T = TypeVar("_T")


class Dispatcher(Generic[_P, _T]):
    def __init__(self, context: Context) -> None:
        self._context = context
        self._handlers: dict[Any, Callable] = {}

    def on(self, name: Any, handler: Callable[_P, Awaitable[_T]]):
        if name in self._handlers:
            raise ValueError(f"Handler for {name} already exists")
        
        self._handlers[name] = self._context.inject(handler)

    async def __call__(self, name: Any, *args: _P.args, **kwds: _P.kwargs) -> Awaitable[_T]:
        return await self._handlers[name](*args, **kwds)


class DispatcherDescriptor(Generic[_P, _T]):
    def __get__(self, instance: "TransportFeature", owner) -> Dispatcher[_P, _T]:
        return instance.__dict__.setdefault(self.name, Dispatcher(instance.context))

    def __set__(self, instance: "TransportFeature", value: Dispatcher[_P, _T]) -> None:
        pass

    def __set_name__(self, owner, name):
        self.name = name


def dispatcher(_: Callable[_P, _T]) -> DispatcherDescriptor[_P, _T]:
    return DispatcherDescriptor()
