from typing import Iterable
from uuid import uuid4
from string import ascii_letters


class Cookies:
    def __init__(self, cookie_string: str):
        self.cookies = dict[str, str]()
        self._parse(cookie_string)

    def _parse(self, cookie_string: str):
        if not cookie_string:
            return

        for cookie in cookie_string.split(";"):
            key, value = cookie.split("=")
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


ascii_length = len(ascii_letters)


def short_uuid(length=12):
    original_uuid = uuid4()
    hex_string = original_uuid.hex
    base62_uuid = ""
    for i in range(0, len(hex_string), 2):
        hex_byte = int(hex_string[i : i + 2], 16)
        base62_uuid += ascii_letters[hex_byte % ascii_length]

    short_uuid = base62_uuid[:length]

    return short_uuid


def validate_data(func, *args):
    try:
        from pydantic import BaseModel

        def make_model(cls, data):
            if not issubclass(cls, BaseModel):
                return data

            return cls.model_validate(data)

    except ImportError:

        def make_model(cls, data):
            from dataclasses import is_dataclass

            if is_dataclass(cls):
                return cls(**data)

            return data

    import inspect

    signature = inspect.signature(func)
    parameters = signature.parameters
    if not parameters:
        return args

    args = list(args)
    for i, parameter in enumerate(parameters.values()):
        cls = parameter.annotation
        if not isinstance(cls, type):
            continue

        args[i] = make_model(cls, args[i])

    return args
