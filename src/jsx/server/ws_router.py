from enum import Enum
from .components import COMPONENTS_REPOSITORY
from jsx.renderer import render_json
from jsx.server.database import DB


class WSRouterCommands(str, Enum):
    GET_COMPONENT = "component"


def get_component(socket_id: str, name: str, props={}):
    cls = COMPONENTS_REPOSITORY.get_component(name)
    return "component", render_json(cls(**props))


ws_router = {
    WSRouterCommands.GET_COMPONENT: get_component,
}
