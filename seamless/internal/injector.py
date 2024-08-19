from functools import wraps
from inspect import iscoroutinefunction, signature
from typing import Type, TypeVar, overload, Callable, TypeAlias

T = TypeVar("T")

InjectFactory: TypeAlias = Callable[[], T]


class Injector:
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
                positional_args, keyword_args = self.inject_params(callback)
                args = list(args)
                for i, arg in enumerate(positional_args):
                    if type(arg) not in self.dependencies:
                        positional_args[i] = args.pop(0)
                return await callback(*positional_args, **keyword_args, **kwargs)

        else:

            @wraps(callback)
            def wrapper(*args, **kwargs):
                positional_args, keyword_args = self.inject_params(callback)
                args = list(args)
                for i, arg in enumerate(positional_args):
                    if type(arg) not in self.dependencies:
                        positional_args[i] = args.pop(0)
                return callback(*positional_args, **keyword_args, **kwargs)

        return wrapper

    def inject_params(self, callback: Callable) -> tuple[list, dict]:
        signature_ = signature(callback)
        parameters = signature_.parameters

        positional_args = []
        keyword_args = {}

        for name, parameter in parameters.items():
            if parameter.kind == parameter.POSITIONAL_OR_KEYWORD:
                if parameter.annotation in self.dependencies:
                    positional_args.append(self.dependencies[parameter.annotation]())
                else:
                    positional_args.append(parameter.default)
            elif parameter.kind == parameter.KEYWORD_ONLY:
                if parameter.annotation in self.dependencies:
                    keyword_args[name] = self.dependencies[parameter.annotation]()
                else:
                    keyword_args[name] = parameter.default

        return positional_args, keyword_args


def injectable(factory: InjectFactory | None = None):
    def decorator(cls: Type[T]) -> Type[T]:
        Injector().add(cls, factory or cls())
        return cls

    return decorator


_DEFAULT_INJECTOR = Injector()


def injector():
    return _DEFAULT_INJECTOR
