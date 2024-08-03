from pathlib import Path
from seamless import Component, Span, JS

HERE = Path(__file__).parent


class Clock(Component):
    def render(self):
        return Span(
            init=JS(file=HERE / "clock.js"),
        )
