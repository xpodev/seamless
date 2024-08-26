.. _router:

######
Router
######

The ``Router`` component is used to create a single page application (SPA) with multiple pages.

The router component is used to render different components based on the current path.

.. note:: 
    The ``Router`` component is dependent on the :ref:`client-side Seamless library <seamless-instance>`, so make sure to include the
    script in your ``Page`` component.


Usage
#####

To use the ``Router`` component, create a new instance of the ``Router`` class from ``seamless.components.router``
and add routes to the router using the ``Route`` class.

Assuming you have the following pages in the ``pages`` module:

- Home
- About
- Contact

Home Page Example:

.. code-block:: python
    :caption: Home Page

    # pages.py

    from seamless import Component, Div

    class Home(Component):
        def render(self):
            return Div()(
                "Home Page"
            )


To navigate between the pages, use the ``RouterLink`` component from ``seamless.components.router``.

.. code-block:: python
    :caption: Using the Router component

    # my_app.py

    from seamless import Nav, Div, Component
    from seamless.components.router import Router, Route, RouterLink 
    from pages import Home, About, Contact

    class MyApp(Component):
        def render(self):
            return Div(class_name="root")(
              Nav(
                  RouterLink(to="/")(
                      "Home"
                  ),
                  RouterLink(to="/about")(
                      "About"
                  ),
                  RouterLink(to="/contact")(
                      "Contact"
                  )
              ),
              Div(class_name="content")(
                  Router(
                      Route(path="/", component=Home),
                      Route(path="/about", component=About),
                      Route(path="/contact", component=Contact)
                  )
              )
            )

Then, pass the ``MyApp`` component in the ``Page`` component and render the page.

.. code-block:: python
    :caption: Rendering the page

    # main.py

    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    from seamless import render
    from seamless.middlewares import ASGIMiddleware as SeamlessMiddleware
    from app_page import AppPage
    from my_app import MyApp

    app = FastAPI()
    app.add_middleware(SeamlessMiddleware)

    @app.get("/", response_class=HTMLResponse)
    async def read_root():
        return render(
          AppPage(
            MyApp()
          )
        )

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="localhost", port=8000)


Path Parameters
###############

The ``Route`` component supports path parameters.

To use path parameters, put the parameter name inside curly braces in the path.
Optionally, you can specify a type for the parameter by adding a colon and the type name after the parameter name.

The supported types are:

- ``int``
- ``float``

The parameter will be passed to the component as a prop with the same name.

.. code-block:: python

    # pages.py

    from dataclasses import dataclass
    from seamless import Component, Div

    @dataclass
    class User(Component):
        id: int

        def render(self):
            return Div()(
                f"User Page - {self.id}"
            )


.. code-block:: python
    :caption: Using path parameters

    # my_app.py

    from seamless import Nav, Div, Component
    from seamless.components.router import Router, Route, RouterLink 
    from pages import Home, About, Contact, User

    class MyApp(Component):
        def render(self):
            return Div(class_name="root")(
              Nav(
                  RouterLink(to="/user/1")(
                      "User 1"
                  ),
                  RouterLink(to="/user/2")(
                      "User 2"
                  )
              ),
              Div(class_name="content")(
                  Router(
                      Route(path="/user/{id:int}", component=User)
                  )
              )
            ) 
