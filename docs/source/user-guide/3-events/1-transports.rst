.. _transports:

##########
Transports
##########

Transports are the underlying mechanism that the event system uses to send
messages between the server and the client.

By default, Seamless uses `socket.io <https://socket.io/>`_ as the transport mechanism. This
allows for real-time, bidirectional and event-based communication between the
server and the client.

.. note::
    The transport mechanism is abstracted away from the user, and you do not
    need to interact with it directly. The event system provides a high-level
    API that allows you to send and receive messages without worrying about the
    underlying transport mechanism.

To use the event system, you need to add the transport middleware to your ASGI app and
initialize the event system.

.. code-block:: python
    :caption: Adding the transport middleware

    from fastapi import FastAPI
    from seamless.middlewares import SocketIOMiddleware

    app = FastAPI()
    app.add_middleware(SocketIOMiddleware)

To initialize the event system, in the root component of your application (can be the base page or the main layout)
call the ``SocketIOTransport.init`` method from the ``seamless.extension`` module.

.. code-block:: python
    :caption: Initializing the event system

    from seamless.extension import SocketIOTransport

    class MyPage(Page):
        def body(self):
            return (
              SocketIOTransport.init(),
              *super().body()
            )

This will initialize the event system and make it available to the components.