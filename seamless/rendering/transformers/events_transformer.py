from seamless.context.database import DB

EVENTS_NAMESPACE = "seamless:event"
ELEMENT_ATTR = "seamless:element"

def events_transformer():
    def matcher(key: str, value):
        return key.startswith("on_") and callable(value)

    def event_transformer(key: str, value, element_props):
        if not callable(value):
            element_props[key] = value
            return
        
        event_name = key.removeprefix("on_")
        action = DB.add_event(value)
        element_props[f"{EVENTS_NAMESPACE}:{event_name}"] = action.id
        element_props[ELEMENT_ATTR] = True

    return matcher, event_transformer