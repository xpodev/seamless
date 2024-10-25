from typing import Any, Generic, Callable

from pydom import Context
from pydom.context.feature import Feature
from typing_extensions import ParamSpec

from ...errors import ClientError


_P = ParamSpec("_P")


class Subscriptable(Generic[_P]):
    def __init__(self, context: Context) -> None:
        self._callbacks = []
        self._context = context

    async def __call__(self, *args: _P.args, **kwds: _P.kwargs) -> None:
        try:
            for callback in self._callbacks:
                await callback(*args, **kwds)
        except ClientError as error:
            from .transport import TransportFeature

            transport = self._context.get_feature(TransportFeature)
            await transport.error(error)

    def __iadd__(self, callback: Any) -> "Subscriptable":
        self._callbacks.append(self._context.inject(callback))
        return self


class SubscriptableDescriptor(Generic[_P]):
    def __get__(self, instance: "Feature", owner) -> Subscriptable[_P]:
        return instance.__dict__.setdefault(self.name, Subscriptable(instance.context))

    def __set__(self, instance: "Feature", value: Subscriptable[_P]) -> None:
        pass

    def __set_name__(self, owner, name):
        self.name = name


def event(_: Callable[_P, None]) -> SubscriptableDescriptor[_P]:
    return SubscriptableDescriptor()
