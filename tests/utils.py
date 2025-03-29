from typing import Union
from pathlib import Path

from pydom import render
from pydom.types import Renderable, Primitive

ROOT_DIR = Path(__file__).parent


def test_render_with_file(
    element: Union[Renderable, Primitive],
    file: str,
    *,
    pretty=False,
    **kwargs,
) -> bool:
    lines = []
    with open(ROOT_DIR / file) as f:
        lines = f.readlines()
        if not pretty:
            lines = [line.strip() for line in lines]

    expected = "".join(lines)
    actual = render(element, pretty=pretty, **kwargs)

    return expected == actual
