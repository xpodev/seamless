from seamless.internal import SEAMLESS_ELEMENT_ATTRIBUTE, SEAMLESS_INIT_ATTRIBUTE

def events_transformer():

    def matcher(key: str, value):
        return key.startswith("on_") and callable(value)

    def event_transformer(key: str, value, props):
        from seamless.context.database import DB

        if not callable(value):
            props[key] = value
            return
        
        event_name = key.removeprefix("on_")
        action = DB.add_event(value)
        props[SEAMLESS_INIT_ATTRIBUTE] = props.get(SEAMLESS_INIT_ATTRIBUTE, "") + \
        f"""this.addEventListener('{event_name}', (event) => {{
            const outEvent = seamless.instance.eventObjectTransformer(
              event, 
              seamless.instance.serializeEventObject(event)
            );
          seamless.instance.socket.emit("event", "{action.id}", outEvent);
        }});"""

        props[SEAMLESS_ELEMENT_ATTRIBUTE] = True
        del props[key]

    return matcher, event_transformer

def js_events_transformer():
    def matcher(key: str, value):
        return key.startswith("on_") and isinstance(value, str)

    def event_transformer(key: str, value, element_props):       
        event_name = key.removeprefix("on_")
        element_props[f"on{event_name}"] = value
        del element_props[key]

    return matcher, event_transformer