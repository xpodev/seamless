.. _page:

####
Page
####

The page component is a the top-level component that represents a web page.
It is a container that holds all the other components that will be rendered on the page.

The default page component includes the components for the following HTML structure:

.. code-block:: html

  <!DOCTYPE html>
  <html>
    <head lang="en">
      <meta charset="UTF-8">
      <meta name="viewport" content="width=devi
      ce-width, initial-scale=1.0">
      <title>
        <!-- The page title property -->
      </title>
    </head>
    <body dir="ltr">
      <!-- Page children go here -->
    </body>
  </html>

Usage
#####

The page component can be used to create a new page by passing the following properties:

- ``title``: The page's title
- ``html_props``: The props to insert inside the ``html`` tag
- ``head_props``: The props to insert inside the ``head`` tag
- ``body_props``: The props to insert inside the ``body`` tag

.. code-block:: python

    from seamless import Div, P
    from seamless.components import Page

    def my_awesome_page():
        return Page(title="My awesome page")(
            Div(class_name="container mt-5")(
              Div(class_name="text-center p-4 rounded")(
                Div(class_name="h-1")(
                  "Awesome page"
                ),
                P(class_name="lead")(
                  "Welcome to seamless"
                )
              )
            )
          )
        

Custom Pages
############

You can create custom pages by extending the page component and overriding the default ``head`` and ``body`` methods.

.. code-block:: python

    from seamless import Div, Link
    from seamless.components import Page

    class MyPage(Page):
        def head(self):
            return (
                *super().head(), # Include the default head components
                Link(
                  rel="stylesheet",
                  href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                )
            )

        def body(self):
            return (
              Div(id="root")( # Wrap all the page children in a div with id root
                *self.children
              )
            )

    def my_awesome_page():
        return MyPage(title="My awesome page")(
            Div(class_name="container mt-5")(
              Div(class_name="text-center p-4 rounded")(
                Div(class_name="h-1")(
                  "Awesome page"
                ),
                P(class_name="lead")(
                  "Welcome to seamless"
                )
              )
            )
        )

.. note:: 
  Both ``head`` and ``body`` methods should return an iterable of components, elements or primitives that will
  be rendered inside the ``<head>`` and ``<body>`` tags respectively.

API Reference
#############

+------------+--------+---------------------------------------------+----------------------+
| Name       | Type   | Description                                 | Default value        |
+============+========+=============================================+======================+
| title      | string | The page's title                            | ``None``             |
+------------+--------+---------------------------------------------+----------------------+
| html_props | dict   | The props to insert inside the ``html`` tag | ``{ "lang": "en" }`` |
+------------+--------+---------------------------------------------+----------------------+
| head_props | dict   | The props to insert inside the ``head`` tag | ``{}``               |
+------------+--------+---------------------------------------------+----------------------+
| body_props | dict   | The props to insert inside the ``body`` tag | ``{ "dir": "ltr" }`` |
+------------+--------+---------------------------------------------+----------------------+
