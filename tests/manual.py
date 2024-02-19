from .components import App
from jsx.renderer import render
from pprint import pprint

print(render(App(), prettify=True))
pprint(App().to_json())