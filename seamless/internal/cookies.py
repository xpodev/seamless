# type: ignore

from typing import Iterable

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
