from enum import Enum
from seamless.rendering.json import to_dict
from seamless.errors import ActionError
from .database import DB
from .components import COMPONENTS_REPOSITORY


class WSRouterCommands(str, Enum):
    GET_COMPONENT = "component"
    EVENT = "event"


def get_component(sid: str, name: str, props={}):
    cls = COMPONENTS_REPOSITORY.get_component(name)
    return to_dict(cls(**props))


async def event(sid: str, data: str, event_data: dict):
    await DB.invoke_event(data, event_data, scope=sid)


ws_router = {
    WSRouterCommands.GET_COMPONENT: get_component,
    WSRouterCommands.EVENT: event,
}
