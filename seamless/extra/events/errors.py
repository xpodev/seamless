from ...errors import Error, ClientError

class ActionError(Error):
    """
    Raised when an error occurs while invoking an action.
    """
    ...


class EventNotFoundError(ClientError):
    """
    Raised when an event is not found.
    """
    ...