from typing import Generic, TypeVar, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from seamless.types.styling.css_properties import CSSProperties

T = TypeVar("T")


class Style:
    class _StyleProperty(Generic[T]):
        def __init__(self, instance: "Style", name: str):
            self.instance = instance
            self.name = name.replace("_", "-")

        def __call__(self, value: T):
            self.instance.style[self.name] = value
            return self.instance

    def __init__(self, *styles: "Style | dict", **kwargs: Unpack["CSSProperties"]):
        self.style: dict[str, object] = {}
        for style in styles:
            if isinstance(style, Style):
                style = style.style
            self.style.update(style)
        self.style.update(kwargs)
        self.style = {
            k.replace("_", "-"): v for k, v in self.style.items() if v is not None
        }

    def copy(self):
        return Style(self)

    def to_css(self):
        return "".join(map(lambda x: f"{x[0]}:{x[1]};", self.style.items()))

    def __str__(self):
        return self.to_css()

    def __getattr__(self, name: str):
        return Style._StyleProperty(self, name)