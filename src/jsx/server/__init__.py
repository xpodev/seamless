from socketio import AsyncServer, ASGIApp
from .database import ElementsDatabase


db = ElementsDatabase()
server = AsyncServer(async_mode="asgi")


@server.event
async def dom_event(sid, data, event_data):
    component_id, event = data.split(":")
    component_id = component_id
    db.invoke_component_event(component_id, event, event_data)


@server.event
async def connect(sid, environ):
    print("connect", sid)


def mount(
    app,
    socket_path="/socket.io",
    scripts_path="/_jsx"
):
    app.mount(socket_path, ASGIApp(server))
