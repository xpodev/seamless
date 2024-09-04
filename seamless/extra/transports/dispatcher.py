from typing import Any, Callable, Dict, Generic, TYPE_CHECKING, TypeVar, Awaitable

from pydom import Context
from typing_extensions import ParamSpec


if TYPE_CHECKING:
    from .transport import TransportFeature

P = ParamSpec("P")
T = TypeVar("T")


class Dispatcher(Generic[P, T]):
    def __init__(self, context: Context) -> None:
        self._context = context
        self._handlers: Dict[Any, Callable] = {}

    def on(self, name: Any, handler: Callable[P, Awaitable[T]]):
        if name in self._handlers:
            raise ValueError(f"Handler for {name} already exists")
        
        self._handlers[name] = self._context.inject(handler)

    async def __call__(self, name: Any, *args: P.args, **kwds: P.kwargs) -> Awaitable[T]:
        return await self._handlers[name](*args, **kwds)


class DispatcherDescriptor(Generic[P, T]):
    def __get__(self, instance: "TransportFeature", owner) -> Dispatcher[P, T]:
        return instance.__dict__.setdefault(self.name, Dispatcher(instance.context))

    def __set__(self, instance: "TransportFeature", value: Dispatcher[P, T]) -> None:
        pass

    def __set_name__(self, owner, name):
        self.name = name


def dispatcher(_: Callable[P, T]) -> DispatcherDescriptor[P, T]:
    return DispatcherDescriptor()
