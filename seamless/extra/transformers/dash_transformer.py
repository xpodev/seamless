def dash_transformer():
    def matcher(key: str, value):
        return "_" in key and (isinstance(value, (str, int, float)) or value is None)
    
    def transformer(key, value, props):
        dash_key = key.replace("-", "_")
        props[dash_key] = value
        del props[key]

    return matcher, transformer