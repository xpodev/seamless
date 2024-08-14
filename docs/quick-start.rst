Quick Start
###########

This is a quick start guide to get you up and running with Seamless.
The guide will show you how to setup Seamless and integrate it with `FastAPI <https://fastapi.tiangolo.com/>`_.

Installation
============

First, we need to install the Seamless package.

.. code-block:: bash

    $ pip install python-seamless


Create Reusable Page
====================

Seamless provides a default page component that is the minimal structure for a web page.

Since we want bootstrap to be included in all of our pages, we will create a new page component
that extends the default page component and adds a link to the bootstrap stylesheet.

More information about the default page component can be found `here <components/page.html>`_.

.. code-block:: python
    :caption: Creating a custom page component

    # page.py    

    from seamless import Link
    from seamless.components.page import Page

    class AppPage(Page):
      def head(self):
        return (
          *super().head(),
          Link(
            rel="stylesheet",
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
          )
        )


Last, we create the ``FastAPI`` app and add an endpoint that will render our page when the user is accessing the root route.

.. code-block:: python
    :caption: Creating the FastAPI app

    # main.py

    from fastapi import FastAPI
    from fastapi.responses import HTMLResponse
    from seamless import render, Div, P
    from page import AppPage

    app = FastAPI()

    @app.get("/", response_class=HTMLResponse)
    async def read_root():
        return render(
          AppPage(
            Div(class_name="container mt-5")(
              Div(class_name="text-center p-4 rounded")(
                Div(class_name="display-4")(
                  "Hello, World!"
                ),
                P(class_name="lead")(
                  "Welcome to seamless"
                )
              )
            )
          )
        )

    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="localhost", port=8000)

That's it! Now you can run the app and access it at `http://localhost:8000/ <http://localhost:8000/>`_.

It should display a page like this:

.. image:: _static/images/quick-start.jpeg
    :alt: Quick Start
    :align: center