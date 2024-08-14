.. _asg-middleware:

###############
ASGI Middleware
###############

The ``ASGIMiddleware`` class is the middleware that handles all the linked actions between the
frontend components and the backend functions.

When linking a python function to a frontend component, the ``ASGIMiddleware`` middleware must be
added to the ASGI application.

.. code-block:: python
  :caption: Adding the ASGIMiddleware to the ASGI application

  from fastapi import FastAPI
  from seamless.middlewares import ASGIMiddleware as SeamlessMiddleware

  app = FastAPI()
  app.add_middleware(SeamlessMiddleware)

