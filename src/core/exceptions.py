from apiflask import HTTPError


# https://apiflask.com/error-handling/
class ApplicationError(HTTPError):
    status_code = 500
    message = "Service Unavailable"
