_SIMPLE_TRANSFORMERS = {
    "html_for": "for",
    "accept_charset": "accept-charset",
    "http_equiv": "http-equiv",
    "access_key": "accesskey",
    "content_editable": "contenteditable",
    "cross_origin": "crossorigin",
    "tab_index": "tabindex",
    "use_map": "usemap",
    "col_span": "colspan",
    "row_span": "rowspan",
    "char_set": "charset",
}


def simple_transformer():
    def matcher(key: str, _):
        return key in _SIMPLE_TRANSFORMERS

    def transformer(key: str, value, element):
        element.props[_SIMPLE_TRANSFORMERS[key]] = value
        del element.props[key]

    return matcher, transformer
