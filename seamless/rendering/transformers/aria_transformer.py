from . import transformer_for

@transformer_for(lambda key, _: key.startswith("aria_"))
def aria_transformer(key, value, props):
    aria_key = key.replace("_", "-")
    props[aria_key] = value
    del props[key]