# type: ignore

from functools import wraps as _wraps
from inspect import iscoroutinefunction, ismethod
from string import ascii_letters
from typing import TypeGuard
from uuid import uuid4

ascii_length = len(ascii_letters)


class Promise:
    def __init__(self, value):
        self.value = value

    def __await__(self):
        return getattr(self.value, "__await__", lambda: self.value or iter(()))()


class TwoWayDict(dict):
    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        if value in self:
            del self[value]
        dict.__setitem__(self, key, value)
        dict.__setitem__(self, value, key)

    def __delitem__(self, key):
        dict.__delitem__(self, self[key])
        dict.__delitem__(self, key)

    def __len__(self):
        """Returns the number of connections"""
        return dict.__len__(self) // 2


def short_uuid(length=12):
    original_uuid = uuid4()
    hex_string = original_uuid.hex
    base62_uuid = ""
    for i in range(0, len(hex_string), 2):
        hex_byte = int(hex_string[i : i + 2], 16)
        base62_uuid += ascii_letters[hex_byte % ascii_length]

    short_uuid = base62_uuid[:length]

    return short_uuid


def to_iter(value):
    try:
        return iter(value)
    except TypeError:
        return iter((value,))


def to_async(func):
    if iscoroutinefunction(func):
        return func

    @wraps(func)
    async def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


class _obj(object):
    def __init__(self, d: dict):
        for key, value in d.items():
            if isinstance(key, (list, tuple)):
                setattr(
                    self, key, [_obj(x) if isinstance(x, dict) else x for x in value]
                )
            else:
                setattr(self, key, _obj(value) if isinstance(value, dict) else value)


def wraps(info):
    def inner(callback):
        if ismethod(info):

            if iscoroutinefunction(callback):

                @_wraps(info.__func__)
                async def wrapper(_, *args, **kwargs):
                    return await callback(*args, **kwargs)

            else:

                @_wraps(info.__func__)
                def wrapper(_, *args, **kwargs):
                    return callback(*args, **kwargs)

            return wrapper.__get__(info.__self__, info.__class__)

        if iscoroutinefunction(callback):

            @_wraps(info)
            async def wrapper(*args, **kwargs):
                return await callback(*args, **kwargs)

        @_wraps(info)
        def wrapper(*args, **kwargs):
            return callback(*args, **kwargs)
        
        return wrapper

    return inner


def is_primitive(value) -> TypeGuard[str | int | float | bool | None]:
    return isinstance(value, (str, int, float, bool)) or value is None
