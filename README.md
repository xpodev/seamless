# Python JSX

![build](https://github.com/xpodev/pyrl/actions/workflows/python-publish.yml/badge.svg)
![test](https://github.com/xpodev/pyrl/actions/workflows/python-test.yml/badge.svg)

JSX is a Python package for creating and manipulating HTML components. It is working similar to React.js, but in Python.


## Usage

```python
from jsx import Div, H1, P, Component, Style

class MyComponent(Component):
  def render(self):
    return Div(
      H1(
        "Hello, World!",
        style=Style(
          color="#33343c"
        ),
      ),
      P(
        "Welcome to JSX!"
      ),
      style=Style(
        text_align="center"
      )
    )
```
```python
from .components import MyComponent
from jsx.renderer import render

@app.get("/")
def hello_world():
  return render(MyComponent())
```

### Server actions
It's possible to pass a python function as component props.

The current version works only with `ASGIApp`.
```python
class Person(Component):
  def __init__(self, name: str, age: float):
    self.age = age
    self.name = name

  def render(self):
    return Form(
      Div(f"Update the age for {name}"),
      Label(
        "Age: ",
        html_for="age"
      ),
      Input(
        type="text",
        on_change=self.set_age
      ),
      Button(
        "Submit Age",
        type="submit"
      ),
      on_submit=self.save_age
    )

  def set_age(self, event_data: JSXChangeEvent):
    self.age = event_data.value

  def save_age(self, event_data: JSXSubmitEvent):
    user = get_user()
    user.age = self.age
    save(user)
```
To call a function on the server include this script in your file
```html
<script src="/_jsx/scripts/main.js"></script>
```
In your ASGI app call the `mount` function from the `jsx.server` module
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from jsx.server import JSXServer

app = FastAPI()
jsx_server = JSXServer(cors_allowed_origins="*")
app.mount("/_jsx/scripts", StaticFiles(directory=jsx_server.scripts_path()), name="scripts")
jsx_server.mount(app, socket_path="/socket.io")
```
You can pass the following config to the `mount` to change the path of all jsx endpoints.
```python
jsx_server.mount(app, socket_path="/jsx.io", scripts_path="/static/jsx")
```
The actions use [socket.io](https://socket.io) to communicate between server and client.

## TODO
- [ ] Add detailed documentation
- [ ] Add more tests

## Contributing
Feel free to open an issue or a pull request.