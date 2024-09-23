.. _dynamic-pages:

#############
Dynamic Pages
#############

Seamless is much more than a static site generator.
It is a full-featured library that allows you to create dynamic web pages.

Dynamic pages offer the following features:

- **Dynamic Content**: The content of the page can change based on user input or other events.
- **Client-Side Rendering**: The page can be updated without reloading the entire page.
- **State Management**: The state of the page can be managed and updated.
- **Event Handling**: Events can be handled on the client side and trigger actions on the server side.

To create a dynamic page, you need to include the Seamless core script in your HTML file.
This script provides the necessary functionality to create and manage dynamic pages.

The core script is available at the following URL:

.. code-block:: html
  :substitutions:

  <script src="https://cdn.jsdelivr.net/npm/@python-seamless@|version|/umd/seamless.min.js"></script>

This allows you to initialize the Seamless instance on the client side and start creating dynamic pages.

.. code-block:: html
  :name: seamless-instance
  :caption: Initializing Seamless  

  <script>
    const seamless = new Seamless();
  </script>


Also, there is an init script that initializes the Seamless instance without the need to write any JavaScript code.

.. code-block:: html
  :substitutions:

  <script src="https://cdn.jsdelivr.net/npm/@python-seamless@|version|/umd/seamless.init.js"></script>

Usage in Seamless
#################

To add the script in all of your pages, you can create a new page component that extends the default page component
and adds the script to the head.

It is recommended to add ``defer`` to the script tag to ensure that the script is executed after the page is loaded, or 
alternatively, you can add the script at the end of the body tag.

.. code-block:: python
  :substitutions:

  # app_page.py

  from seamless import Script
  from seamless.components.page import Page

  class AppPage(Page):
    def head(self):
      return (
        *super().head(),
        Script(src="https://cdn.jsdelivr.net/npm/python-seamless@|version|/umd/seamless.min.js")
      )