import re

_pascal_case_to_snake_case_compiled = re.compile(r"(?<!^)(?=[A-Z])")


def pascal_case_to_snake_case(title_case: str) -> str:
    return _pascal_case_to_snake_case_compiled.sub("_", title_case).lower()


class JSONToObject:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


def make_object(data):
    if isinstance(data, dict):
        return JSONToObject(**data)
    if isinstance(data, list):
        return [make_object(x) for x in data]

    return data
