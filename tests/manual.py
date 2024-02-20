from .components import App
from jsx.renderer import render, render_json
from pprint import pprint

print(render(App(), prettify=True))
pprint(render_json(App()))