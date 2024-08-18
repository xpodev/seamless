![Seamless](https://github.com/xpodev/seamless/blob/main/images/seamless.png?raw=true)

[![PyPI version](https://badge.fury.io/py/python-seamless.svg?)](https://pypi.org/project/python-seamless)

![test](https://github.com/xpodev/pyrl/actions/workflows/python-test.yml/badge.svg)

Seamless is a Python package for creating and manipulating HTML components. It is working similar to React.js, but in Python.

We have detailed documentation [here](https://seamless.readthedocs.io/)

## Installation
```sh
pip install python-seamless
```

## Usage

```python
from seamless import Div, H1, P, Component, StyleObject

class MyComponent(Component):
  def render(self):
    root_style = StyleObject(color="#33343c")
    return Div(style=div_style)(
      H1(
        "Hello, World!",
      ),
      P(
        "Welcome to Seamless!"
      ),
    )
```
```python
from .components import MyComponent
from seamless.renderer import render

@app.get("/")
def hello_world():
  return render(MyComponent())
```

### Server actions
It's possible to pass a python function as component props.

The current version works with `ASGIApp`.
```python
class Person(Component):
  def __init__(self, name: str, age: float):
    self.age = age
    self.name = name

  def render(self):
    return Form(on_submit=self.save_age)(
      Div(f"Update the age for {name}"),
      Label(html_for="age")(
        "Age: "
      ),
      Input(
        type="text",
        on_change=self.set_age
      ),
      Button(type="submit")(
        "Submit Age"
      ),
    )

  def set_age(self, event_data: ChangeEvent):
    self.age = event_data.value

  def save_age(self, event_data: SubmitEvent):
    user = get_user()
    user.age = self.age
    save(user)
```
To call a function on the server include this script in your file
```html
<script src="https://cdn.jsdelivr.net/npm/@python-seamless/core@0.8.4/umd/seamless.init.js"></script>
```
Import the middleware and mount it to your app
```python
from fastapi import FastAPI
from seamless.middlewares import ASGIMiddleware as SeamlessMiddleware

app = FastAPI()
app.add_middleware(SeamlessMiddleware)
```
You can pass the following config to the middleware to change the socket path of all seamless endpoints.
```python
app.add_middleware(
  SeamlessMiddleware,
  socket_path="/my/custom/path"
)
```
Actions use [socket.io](https://socket.io) to communicate between server and client.

## TODO
- [x] Add detailed documentation
- [ ] Add more tests
- [ ] Add support for http actions

## Contributing
Feel free to open an issue or a pull request.
