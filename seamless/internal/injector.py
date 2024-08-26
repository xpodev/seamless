from inspect import iscoroutinefunction, signature
from typing import Type, TypeVar, overload, Callable, TypeAlias

from ..internal.utils import wraps

T = TypeVar("T")

InjectFactory: TypeAlias = Callable[[], T]


class Injector:
    """
    A simple dependency injection container

    To get an instance of a class, you can use the `injector` property of the `Context` class.
    """

    def __init__(self):
        self.dependencies = dict[type, Callable]()

    @overload
    def add(self, cls: Type[T], factory: Callable[[], T], /) -> None: ...
    @overload
    def add(self, cls: Type[T], instance: T, /) -> None: ...

    def add(self, cls: Type[T], dependency: Callable[[], T] | T, /) -> None:
        self.dependencies[cls] = (
            dependency if callable(dependency) else lambda: dependency
        )

    def inject(self, callback: Callable) -> Callable:
        if iscoroutinefunction(callback):

            @wraps(callback)
            async def wrapper(*args, **kwargs):  # type: ignore
                keyword_args = self.inject_params(callback)
                return await callback(*args, **keyword_args, **kwargs)

        else:

            @wraps(callback)
            def wrapper(*args, **kwargs):
                keyword_args = self.inject_params(callback)
                return callback(*args, **keyword_args, **kwargs)

        return wrapper

    def inject_params(self, callback: Callable):
        signature_ = signature(callback)
        parameters = signature_.parameters

        keyword_args = {}

        for name, parameter in parameters.items():
            if parameter.kind == parameter.POSITIONAL_OR_KEYWORD:
                if parameter.annotation in self.dependencies:
                    keyword_args[name] = self.dependencies[parameter.annotation]()
            elif parameter.kind == parameter.KEYWORD_ONLY:
                if parameter.annotation in self.dependencies:
                    keyword_args[name] = self.dependencies[parameter.annotation]()

        return keyword_args


def injectable(factory: InjectFactory | None = None):
    def decorator(cls: Type[T]) -> Type[T]:
        Injector().add(cls, factory or cls())
        return cls

    return decorator
