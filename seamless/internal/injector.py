from functools import wraps
from inspect import iscoroutinefunction, signature
from typing import Type, TypeVar, overload, Callable

T = TypeVar('T')

class Injector:
  def __init__(self):
    self.dependencies = dict[type, Callable]()


  @overload
  def add(self, cls: Type[T], factory: Callable[[], T], /) -> None: ...
  @overload
  def add(self, cls: Type[T], instance: T, /) -> None: ...

  def add(self, cls: Type[T], dependency: Callable[[], T] | T, /) -> None:
    self.dependencies[cls] = dependency if callable(dependency) else lambda: dependency
