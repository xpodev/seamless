from ...errors import ClientError


class TransportConnectionRefused(ClientError):
    """
    Raised when the connection to the transport is refused.
    """
    pass
