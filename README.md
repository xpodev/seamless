# PyV Module

PyV is a Python package for creating and manipulating HTML components. It is working similar to React.js, but in Python.

## Usage

```python
from pyv import Div, H1, P, Component, Style

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
        "Welcome to PyV!"
      ),
      style=Style(
        text_align="center"
      )
    )
```
```python
from .components import MyComponent
from pyv.renderer import render

@app.get("/")
def hello_world():
  return render(MyComponent())
```

### Server actions
It's possible to pass a python function as component props
```python
class MyComponent(Component):
  def __init__(self, **props):
    super().__init__(props)
    self.age: int = None

  def render(self):
    return Form(
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

  def set_age(self, event_data: PyvChangeEvent):
    self.age = event_data.value

  def save_age(self, event_data: PyvSubmitEvent):
    user = get_user()
    user.age = self.age
    save(user)
```
To call a function on the server include this script in your file
```html
<script src="/_pyv/all.js"></script>
```
In your ASGI app call the `mount` function from the `pyv.server` module
```python
from fastapi import FastAPI
from pyv.server import mount

app = FastAPI()
mount(app)
```
You can pass the following config to the `mount` to change the path of all pyv endpoints.
```python
mount(app, socket_path="/pyv.io", scripts_path="/static/pyv")
```
The actions use [socket.io](https://socket.io) to communicate between server and client.
