from os import PathLike
from typing import overload


class JavaScript:
    @overload
    def __init__(self, code: str, *, async_: bool = False) -> None: ...
    @overload
    def __init__(self, *, file: str | PathLike, async_: bool = False) -> None: ...

    def __init__(self, code=None, *, file=None, async_: bool = False) -> None:
        if file:
            if code:
                raise ValueError("Cannot specify both code and file")
            with open(file, "r") as f:
                code = f.read()
        elif not code:
            raise ValueError("Must specify either code or file")
        self.code = code
        self.async_ = async_

    def __add__(self, other: "JavaScript | str") -> "JavaScript":
        if isinstance(other, JavaScript):
            return JavaScript(self.code + other.code, async_=self.async_ or other.async_)
        elif isinstance(other, str):
            return JavaScript(self.code + other, async_=self.async_)
        else:
            raise TypeError(
                f"Cannot concatenate JavaScript with {type(other).__name__}"
            )


JS = JavaScript
