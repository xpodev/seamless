from typing import Union, overload
import unittest

from pydom import render
from pydom.types.rendering import Primitive, Renderable

from .utils import test_render_with_file


class TestCase(unittest.TestCase):
    @overload
    def assertRender(
        self,
        component: Union[Renderable, Primitive],
        expected: Union[str, dict],
        /,
        **kwargs
    ): ...
    @overload
    def assertRender(
        self,
        component: Union[Renderable, Primitive],
        /,
        *,
        file: str,
        **kwargs
    ): ...

    def assertRender(self, component, expected=None, *, file=None, **kwargs):
        if expected is not None:
            self.assertEqual(render(component, **kwargs), expected)
        elif file is not None:
            self.assertTrue(test_render_with_file(component, file))
        else:
            raise ValueError("Expected or file must be provided")
