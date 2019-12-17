"""
Errors raised by the application
"""
from starlette.exceptions import HTTPException

class EmptyParamError(HTTPException):
    """ Error is raised when group name is not provided. """
    status_code = 400
    message = "Missing Group Name"

class InvalidUsage(HTTPException):
    status_code = 400
    message = "Invalid usage of the method"
