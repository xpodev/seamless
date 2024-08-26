def html_events_transformer():
    def matcher(key: str, value):
        return key.startswith("on_") and isinstance(value, str)

    def transformer(key: str, value, element):       
        event_name = key.replace("_", "").lower()
        element.props[event_name] = value
        del element.props[key]

    return matcher, transformer