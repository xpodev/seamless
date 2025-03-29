from pydom import render, Div, Component
from components import App, Page
from pydom.context.context import get_context
import pydom.context.standard.transformers as t
from pydom.context.standard.transformers.class_transformer import ClassTransformer
from pydom.rendering.render_state import RenderState
from utils import test_render_with_file

context = get_context()


class User: ...


def get_user():
    return {"name": "John Doe"}


context.injector.add(User, get_user)

class Foo(Component):
    def render(self):
        foo()
        return Div("Hello, world!")

@context.inject
def foo(user: RenderState):
    print(user)

render(Foo())

foo()
