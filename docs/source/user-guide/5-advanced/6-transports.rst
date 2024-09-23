.. _advanced-transports:

##########
Transports
##########

This section explains how to create custom transports for the event system.
If you want to use the default transport, you can go to the :ref:`transports` section.

Transports are features that allow you to send messages between the server and the client.

Creating a Transport
####################

Creating a transport is like creating any other feature in Seamless.
You need to create a new class that extends the ``TransportFeature`` class from
the ``seamless.extra.transports`` module.

