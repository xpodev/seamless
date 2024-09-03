from typing import Callable

from pydom.context import Context
from pydom.rendering.render_state import RenderState
from pydom.rendering.tree.nodes import ContextNode

from .database import EventsDatabase, Action
from ..feature import Feature
from ...internal.constants import (
    SEAMLESS_ELEMENT_ATTRIBUTE,
    SEAMLESS_INIT_ATTRIBUTE,
)

from ...internal.validation import wrap_with_validation
from ..transports.errors import TransportConnectionRefused
from ..transports.transport import TransportFeature


class EventsFeature(Feature):
    def __init__(self, context: Context):
        super().__init__(context)

        try:
            self.transport = context.get_feature(TransportFeature)
        except KeyError:
            raise ValueError(
                "EventsFeature requires a TransportFeature in the context."
                "Please add it before adding the EventsFeature."
            )

        self.DB = EventsDatabase()
        self.context.add_prop_transformer(*self._events_transformer())
        self.context.add_post_render_transformer(self._post_render_transformer)

        self.transport.disconnect += self._on_disconnect
        self.transport.event.on("event", self._event)

    async def _event(self, client_id: str, event_id: str, *event_data):
        return await self.DB.invoke_event(event_id, *event_data, scope=client_id)

    async def _on_disconnect(self, client_id: str):
        self.DB.release_actions(client_id)

    def _events_transformer(self):

        def matcher(key: str, value):
            return key.startswith("on_") and callable(value)

        def transformer(
            key: str,
            value: Callable,
            element: ContextNode,
            render_state: RenderState,
        ):
            event_name = key.removeprefix("on").replace("_", "").lower()
            action = Action(
                wrap_with_validation(self.context.inject(value), context=self.context),
                str(hash(value)),
            )

            render_state.custom_data.setdefault("events.actions", []).append(action)

            element.props[SEAMLESS_INIT_ATTRIBUTE] = (
                str(element.props.get(SEAMLESS_INIT_ATTRIBUTE, ""))
                + f"""
                this.addEventListener('{event_name}', (event) => {{
                    const outEvent = seamless.instance.eventObjectTransformer(
                        event, 
                        seamless.instance.serializeEventObject(event)
                    );
                    seamless.emit("event", "{action.id}", outEvent);
                }});
                """
            )

            element.props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
            del element.props[key]

        return matcher, transformer

    def _post_render_transformer(self, root: ContextNode, render_state: RenderState):
        actions = render_state.custom_data.get("events.actions", [])

        if len(actions) == 0:
            return

        client_id = render_state.custom_data.get("transports.client_id", None)

        if not client_id:
            raise ValueError(
                "transports.client_id is not set in the custom_data. "
                "Please make sure that the TransportFeature is added to the context "
                "and TransportFeature.init() is called inside your component."
            )
        else:
            for action in actions:
                self.DB.add_event(action, scope=client_id)
