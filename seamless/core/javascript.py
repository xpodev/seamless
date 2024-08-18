from os import PathLike
from typing import overload


class JavaScript:
    @overload
    def __init__(self, code: str) -> None: ...
    @overload
    def __init__(self, *, file: str | PathLike) -> None: ...

    def __init__(self, code=None, *, file=None) -> None:
        if file:
            if code:
                raise ValueError("Cannot specify both code and file")
            with open(file, "r") as f:
                code = f.read()
        elif not code:
            raise ValueError("Must specify either code or file")
        self.code = code

    def __add__(self, other: "JavaScript | str") -> "JavaScript":
        if isinstance(other, JavaScript):
            return JavaScript(self.code + other.code)
        elif isinstance(other, str):
            return JavaScript(self.code + other)
        else:
            raise TypeError(
                f"Cannot concatenate JavaScript with {type(other).__name__}"
            )


JS = JavaScript
