from ...styling import StyleObject

def style_transformer():
    def matcher(_, value):
        return isinstance(value, StyleObject)
    
    def transformer(key: str, value: StyleObject, element):
        element.props[key] = value.to_css()
    
    return matcher, transformer
