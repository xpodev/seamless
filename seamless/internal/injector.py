from inspect import iscoroutinefunction
from functools import wraps
from typing import TypeVar, Callable, TypeAlias

from pydom.utils.injector import Injector as _Injector


T = TypeVar("T")

InjectFactory: TypeAlias = Callable[[], T]


class Injector(_Injector):
    def inject(self, callback: Callable) -> Callable:
        if iscoroutinefunction(callback):

            @wraps(callback)
            async def wrapper(*args, **kwargs):  # type: ignore
                keyword_args = self.inject_params(callback)
                return await callback(*args, **keyword_args, **kwargs)

            return wrapper

        return super().inject(callback)
