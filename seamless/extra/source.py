from ..internal import short_uuid
from seamless.rendering.transformers import transformer_for


class Source:
    def __init__(self, code: str) -> None:
        self.code = code
        self.id = short_uuid()
        self.rendered = False

    def render(self) -> str:
        if self.rendered:
            return f"{self.id}()"

        self.rendered = True
        return f"function {self.id}(){{{self.code}}}"


@transformer_for(lambda _, value: isinstance(value, Source))
def transform_source(key: str, source: Source, props):
    props["seamless:id"] = source.id
    props["seamless:source:init"] = source.code
