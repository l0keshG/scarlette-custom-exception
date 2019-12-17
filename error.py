
class BaseError(Exception):
    """
    Base class for other errors to extend
    """
    status_code = None
    message = None

    def __init__(self, status_code, description):
        self.description = description
        self.status_code = status_code
        super(BaseError, self).__init__(status_code, description)

    def __str__(self):
        return self.description


class EmptyParamError(BaseError):
    """ Error is raised when group name is not provided. """
    status_code = 400
    message = "Missing Group Name"

class InvalidUsage(BaseError):
    status_code = 400
    message = "ajkashjkashkdj"
