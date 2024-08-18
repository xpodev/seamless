from typing import TYPE_CHECKING

from .database import ElementsDatabase

from ...internal.constants import (
    CLAIM_COOKIE_NAME,
    SEAMLESS_ELEMENT_ATTRIBUTE,
    SEAMLESS_INIT_ATTRIBUTE,
)
from ...internal.cookies import Cookies

if TYPE_CHECKING:
    from ...context import Context


def init_events(ctx: "Context", claim_time=20.0):
    DB = ElementsDatabase(claim_time=claim_time)

    async def event(sid: str, data: str, event_data: dict):
        await DB.invoke_event(data, event_data, scope=sid)

    async def on_connect(sid: str, env: dict):
        cookies = Cookies(env.get("HTTP_COOKIE", ""))
        claim_id = cookies[CLAIM_COOKIE_NAME]
        if not claim_id:
            return await ctx.server.disconnect(sid)

        DB.claim(claim_id, sid)

    async def on_disconnect(sid: str):
        DB.release_actions(sid)

    def events_transformer():

        def matcher(key: str, value):
            return key.startswith("on_") and callable(value)

        def transformer(key: str, value, props):
            event_name = key.removeprefix("on").replace("_", "").lower()
            action = DB.add_event(value)
            props[SEAMLESS_INIT_ATTRIBUTE] = (
                props.get(SEAMLESS_INIT_ATTRIBUTE, "")
                + f"""this.addEventListener('{event_name}', (event) => {{
              const outEvent = seamless.instance.eventObjectTransformer(
                event, 
                seamless.instance.serializeEventObject(event)
              );
            seamless.instance.socket.emit("event", "{action.id}", outEvent);
          }});"""
            )

            props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
            del props[key]

        return matcher, transformer
    
    ctx.add_prop_transformer(*events_transformer())

    ctx.on("connect", on_connect)
    ctx.on("disconnect", on_disconnect)
    ctx.on("event", event)
