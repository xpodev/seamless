# %%
import inspect
import pathlib
import typing

import pydom
import pydom.element
import pydom.types.html

HERE = pathlib.Path(__file__).parent
BASE_STUBS_DIR = HERE / "_auto_html"
PYDOM_ROOT = pathlib.Path(pydom.html.__file__)
SEAMLESS_ROOT = HERE / "seamless/stubs"

pydom_types = {
    x: getattr(pydom.types.html, x)
    for x in dir(pydom.types.html)
    if x.startswith("HTML")
}


element_classes = filter(
    lambda x: isinstance(x, type) and issubclass(x, pydom.element.Element),
    [getattr(pydom.html, x) for x in dir(pydom.html)],
)


def copy_bases(root: pathlib.Path, to_root: pathlib.Path):
    for file in root.rglob("*.pyi"):
        new_file = to_root / file.relative_to(root)
        new_file.parent.mkdir(parents=True, exist_ok=True)
        new_file.write_text(file.read_text())


def init_kwargs_type(cls):
    annotations = inspect.signature(cls.__init__).parameters
    kwargs_hint = annotations.get("kwargs").annotation
    inner = typing.get_args(kwargs_hint)
    if len(inner) != 1:
        return 
    
    inner = inner[0]

    if isinstance(inner, typing.ForwardRef):
        inner = inner.__forward_arg__

    type = pydom_types.get(inner)
    return type


def append_to_init(import_text: str, init_file: pathlib.Path):
    if not init_file.exists():
        init_file.touch()
    lines = init_file.read_text().splitlines()
    lines = [x for x in lines if x.strip()]
    if import_text in lines:
        return
    lines.append(import_text)
    init_file.write_text("\n".join(lines))


copy_bases(
    BASE_STUBS_DIR,
    SEAMLESS_ROOT,
)

for element_cls in element_classes:
    try:
        class_file = pathlib.Path(inspect.getfile(element_cls))

        kwargs_annotations = init_kwargs_type(element_cls)
        annotation_file = None
        if kwargs_annotations:
            annotation_file = pathlib.Path(inspect.getfile(kwargs_annotations))

        element_out_file = SEAMLESS_ROOT / "html" / class_file.with_suffix(".pyi").name
        text = class_file.read_text()
        new_text = text.replace(
            "from ..element import Element",
            "from pydom.element import Element",
        )
        if annotation_file:
            new_text = new_text.replace(
                f"from ..types.html import {kwargs_annotations.__name__}",
                f"from ..types.html.{annotation_file.stem} import {kwargs_annotations.__name__}",
            )
        new_text = new_text.replace(
            "from ..types import ChildType", "from pydom.types import ChildType"
        )

        element_out_file.parent.mkdir(parents=True, exist_ok=True)
        element_out_file.write_text(new_text)

        if annotation_file:
            out_annotation_file = (
                SEAMLESS_ROOT / "types/html" / annotation_file.with_suffix(".pyi").name
            )
            out_annotation_file.parent.mkdir(parents=True, exist_ok=True)
            new_text = annotation_file.read_text().replace(
                "from pydom.types.html.", "from ."
            )
            out_annotation_file.write_text(new_text)

        append_to_init(
            f"from .{element_out_file.stem} import {element_cls.__name__} as {element_cls.__name__}",
            SEAMLESS_ROOT / "html" / "__init__.pyi",
        )

    except Exception as e:
        raise ValueError(f"Error with {element_cls}") from e
