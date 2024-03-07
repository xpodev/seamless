from enum import Enum
from .components import COMPONENTS_REPOSITORY
from jsx.renderer import render_json
from jsx.server.database import DB

class WSRouterCommands(str, Enum):
    GET_COMPONENT = "component"
    CLAIM_ELEMENTS = "claim"


def get_component(socket_id: str, name: str, props={}):
    cls = COMPONENTS_REPOSITORY.get_component(name)
    return "component", render_json(cls(**props))


def claim_elements(socket_id: str, http_id: str):
    DB.claim_http_elements(http_id, socket_id)


ws_router = {
    WSRouterCommands.GET_COMPONENT: get_component,
    WSRouterCommands.CLAIM_ELEMENTS: claim_elements,
}
