from typing import Any, Iterable
from uuid import uuid4
from string import ascii_letters

ascii_length = len(ascii_letters)


class Cookies:
    def __init__(self, cookie_string: str):
        self.cookies = dict[str, str]()
        self._parse(cookie_string)

    def _parse(self, cookie_string: str):
        if not cookie_string:
            return

        for cookie in cookie_string.split(";"):
            key, value = cookie.split("=", maxsplit=1)
            self.cookies[key.strip()] = value.strip()

    def __getitem__(self, key: str):
        return self.cookies[key] if key in self.cookies else None

    def __contains__(self, key: str):
        return key in self.cookies

    @staticmethod
    def from_request_headers(headers: Iterable[Iterable[bytes]] | dict):
        cookie_string = ""
        if isinstance(headers, dict):
            return Cookies(headers.get("cookie", ""))

        for header, value in headers:
            if header == b"cookie":
                cookie_string = value.decode()
                break
        return Cookies(cookie_string)


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


class Promise:
    def __init__(self, value):
        self.value = value

    def __await__(self):
        return getattr(self.value, "__await__", lambda: self.value or iter(()))()


def short_uuid(length=12):
    original_uuid = uuid4()
    hex_string = original_uuid.hex
    base62_uuid = ""
    for i in range(0, len(hex_string), 2):
        hex_byte = int(hex_string[i : i + 2], 16)
        base62_uuid += ascii_letters[hex_byte % ascii_length]

    short_uuid = base62_uuid[:length]

    return short_uuid


def warp_with_validation(func):
    try:
        from pydantic import create_model, ValidationError
    except ImportError:
        return func

    import inspect

    signature = inspect.signature(func)
    parameters = signature.parameters
    if not parameters:
        return func

    func_parameters = {
        name: (
            parameter.annotation if parameter.annotation is not inspect._empty else Any,
            parameter.default if parameter.default is not inspect._empty else None,
        )
        for name, parameter in parameters.items()
    }

    model = create_model(
        "SeamlessModel",
        **func_parameters,
    )

    async def wrapper(*args):
        kwargs = {
            parameter: args[i] for i, parameter in enumerate(func_parameters)
        }

        try:
            data = model(**kwargs)
        except ValidationError as e:
            raise Exception(e.json(include_url=False))

        return await Promise(func(**{name: getattr(data, name) for name in func_parameters}))

    return wrapper
