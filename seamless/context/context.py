from typing import Callable
from seamless.types import Renderable
from .database import ElementsDatabase


class Context:
    def __init__(self, *, claim_time: float) -> None:
        self.db = ElementsDatabase(claim_time=claim_time)

    def on(self, event: str, callback: Callable):
        raise NotImplementedError

    def emit(self, event: str, *args):
        raise NotImplementedError

    def render(self, component: Renderable):
        raise NotImplementedError

    def render_json(self, component: Renderable):
        raise NotImplementedError

    def claim(self, claim_id: str, client_id: str):
        self.db.claim(claim_id, client_id)
