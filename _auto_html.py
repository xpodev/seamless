import pathlib

HERE = pathlib.Path(__file__).parent
HTML_FILES = HERE / "seamless/html"

# with open(HERE / "__init__.py", "w") as f:
#     items = []
#     for file in HERE.iterdir():
#         if file.name.startswith("_") or file.suffix != ".py":
#             continue

#         capitalized = file.stem.capitalize()
#         items.append(capitalized)
#         print(f"from .{file.stem} import {capitalized}", file=f)

#     all = "\n".join(f'\t"{item}",' for item in items)
#     print(f"\n__all__ = [\n{all}\n]", file=f)


html_map = {
    "A": "HTMLAnchorElement",
    "Area": "HTMLAreaElement",
    "Audio": "HTMLAudioElement",
    "Br": "HTMLBRElement",
    "Base": "HTMLBaseElement",
    "Body": "HTMLBodyElement",
    "Button": "HTMLButtonElement",
    "Canvas": "HTMLCanvasElement",
    "Caption": "HTMLTableCaptionElement",
    "Col": "HTMLTableColElement",
    "ColGroup": "HTMLTableColElement",
    "Data": "HTMLDataElement",
    "DataList": "HTMLDataListElement",
    "Del": "HTMLModElement",
    "Details": "HTMLDetailsElement",
    "Dialog": "HTMLDialogElement",
    "Div": "HTMLDivElement",
    "Embed": "HTMLEmbedElement",
    "FieldSet": "HTMLFieldSetElement",
    "Form": "HTMLFormElement",
    "H1": "HTMLHeadingElement",
    "H2": "HTMLHeadingElement",
    "H3": "HTMLHeadingElement",
    "H4": "HTMLHeadingElement",
    "H5": "HTMLHeadingElement",
    "H6": "HTMLHeadingElement",
    "Hr": "HTMLHRElement",
    "Head": "HTMLHeadElement",
    "Heading": "HTMLHeadingElement",
    "Html": "HTMLHtmlElement",
    "IFrame": "HTMLIFrameElement",
    "Image": "HTMLImageElement",
    "Input": "HTMLInputElement",
    "Ins": "HTMLModElement",
    "Li": "HTMLListItemElement",
    "Label": "HTMLLabelElement",
    "Legend": "HTMLLegendElement",
    "Link": "HTMLLinkElement",
    "Map": "HTMLMapElement",
    "Meter": "HTMLMeterElement",
    "Object": "HTMLObjectElement",
    "Ol": "HTMLOrderedListElement",
    "OptGroup": "HTMLOptGroupElement",
    "Option": "HTMLOptionElement",
    "Output": "HTMLOutputElement",
    "P": "HTMLParagraphElement",
    "Param": "HTMLParamElement",
    "Picture": "HTMLPictureElement",
    "Pre": "HTMLPreElement",
    "Progress": "HTMLProgressElement",
    "Q": "HTMLQuoteElement",
    "Script": "HTMLScriptElement",
    "Select": "HTMLSelectElement",
    "Slot": "HTMLSlotElement",
    "Source": "HTMLSourceElement",
    "Span": "HTMLSpanElement",
    "Style": "HTMLStyleElement",
    "Table": "HTMLTableElement",
    "TBody": "HTMLTableSectionElement",
    "Td": "HTMLTableDataCellElement",
    "TFoot": "HTMLTableSectionElement",
    "Th": "HTMLTableHeaderCellElement",
    "THead": "HTMLTableSectionElement",
    "Tr": "HTMLTableRowElement",
    "Template": "HTMLTemplateElement",
    "TextArea": "HTMLTextAreaElement",
    "Time": "HTMLTimeElement",
    "Title": "HTMLTitleElement",
    "Track": "HTMLTrackElement",
    "Ul": "HTMLUnorderedListElement",
    "Video": "HTMLVideoElement",
}

html_classes = [
    "A",
    "Abbr",
    "Address",
    "Area",
    "Article",
    "Aside",
    "Audio",
    "B",
    "Base",
    "Bdi",
    "Bdo",
    "BlockQuote",
    "Body",
    "Br",
    "Button",
    "Canvas",
    "Caption",
    "Cite",
    "Code",
    "Col",
    "ColGroup",
    "Data",
    "DataList",
    "Dd",
    "Del",
    "Details",
    "Dfn",
    "Dialog",
    "Div",
    "Dl",
    "Dt",
    "Em",
    "Embed",
    "FieldSet",
    "FigCaption",
    "Figure",
    "Footer",
    "Form",
    "Fragment",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Head",
    "Header",
    "HGroup",
    "Hr",
    "Html",
    "I",
    "IFrame",
    "Img",
    "Input",
    "Ins",
    "Kbd",
    "Label",
    "Legend",
    "Li",
    "Link",
    "Main",
    "Map",
    "Mark",
    "Menu",
    "Meta",
    "Meter",
    "Nav",
    "NoScript",
    "Object",
    "Ol",
    "OptGroup",
    "Option",
    "Output",
    "P",
    "Param",
    "Picture",
    "Pre",
    "Progress",
    "Q",
    "Rp",
    "Rt",
    "Ruby",
    "S",
    "Samp",
    "Script",
    "Search",
    "Section",
    "Select",
    "Slot",
    "Small",
    "Source",
    "Span",
    "Strong",
    "Style",
    "Sub",
    "Summary",
    "Sup",
    "Svg",
    "Table",
    "TBody",
    "Td",
    "Template",
    "TextArea",
    "TFoot",
    "Th",
    "THead",
    "Time",
    "Title",
    "Tr",
    "Track",
    "U",
    "Ul",
    "Var",
    "Video",
    "Wbr",
]

html_map = {key: html_map.get(key, "HTMLElementProps") for key in html_classes}

template = """from typing import TYPE_CHECKING, Unpack
from ..element import Element

if TYPE_CHECKING:
    from ..types.html import {props_class_name}
    from ..types import ChildType

class {class_name}(Element):
    def __init__(self, *children: "ChildType", **kwargs: Unpack["{props_class_name}"]):
        super().__init__(*children, **kwargs)

    tag_name = "{class_name_lower}"
"""


lower_keys = {key.lower(): key for key in html_map}

for cls, props in html_map.items():
    class_name = cls
    class_name_lower = class_name.lower()
    props_class_name = props
    filename = f"{class_name_lower}.py"

    if class_name == "Meta":
        continue

    if class_name == "Del":
        filename = "del_.py"

    with open(HTML_FILES / filename, "w") as f:
        f.write(template.format(class_name=class_name, class_name_lower=class_name_lower, props_class_name=props_class_name))

    
