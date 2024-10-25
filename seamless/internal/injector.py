from inspect import iscoroutinefunction
from functools import wraps
from typing import TypeVar, Callable

from typing_extensions import TypeAlias

from pydom.utils.injector import Injector as _Injector


_T = TypeVar("_T")

InjectFactory: TypeAlias = Callable[[], _T]


class Injector(_Injector):
    def inject(self, callback: Callable) -> Callable:
        if iscoroutinefunction(callback):

            @wraps(callback)
            async def wrapper(*args, **kwargs):  # type: ignore
                keyword_args = self.inject_params(callback)
                return await callback(*args, **keyword_args, **kwargs)

            return wrapper

        return super().inject(callback)
