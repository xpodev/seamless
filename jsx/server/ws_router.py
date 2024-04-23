from enum import Enum
from .database import DB
from jsx.renderer import render_json
from .components import COMPONENTS_REPOSITORY


class WSRouterCommands(str, Enum):
    GET_COMPONENT = "component"
    DOM_EVENT = "dom_event"


def get_component(sid: str, name: str, props={}):
    cls = COMPONENTS_REPOSITORY.get_component(name)
    return render_json(cls(**props))


async def dom_event(sid: str, data: str, event_data):
    element_id, event = data.split(":")
    try:
        await DB.invoke_element_event(element_id, sid, event, event_data)
    except KeyError:
        raise Exception(f"Element {element_id} not found")


ws_router = {
    WSRouterCommands.GET_COMPONENT: get_component,
    WSRouterCommands.DOM_EVENT: dom_event,
}
