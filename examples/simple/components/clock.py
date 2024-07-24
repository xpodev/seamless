from seamless import Component, Span
from seamless.extra import JS


class Clock(Component):
    def render(self):
        return Span(
            init=JS(
                """setInterval(() => {
            const date = new Date();
            const hours = date.getHours();
            const minutes = date.getMinutes();
            const seconds = date.getSeconds();
            const time = `${hours}:${minutes}:${seconds}`;
            this.innerHTML = time;
        }, 1000)"""
            )
        )
