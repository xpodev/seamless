from functools import wraps
from inspect import iscoroutinefunction, isfunction


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
            if isinstance(value, (list, tuple)):
                setattr(
                    self, key, [_obj(x) if isinstance(x, dict) else x for x in value]
                )
            else:
                setattr(self, key, _obj(value) if isinstance(value, dict) else value)


def is_global(func):
    func = original_func(func)
    return isfunction(func) and (getattr(func, "__closure__", None) is None)


def original_func(func):
    if hasattr(func, "__wrapped__"):
        return original_func(func.__wrapped__)
    return func