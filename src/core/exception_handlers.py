import logging
import sys
import traceback
from enum import Enum
from http import HTTPStatus
from traceback import format_exc

from flask import jsonify, make_response


class AppError(Enum):
    def __init__(self, code: str, message: str, developer_message: str):
        self.code = code
        self.message = message
        self.developer_message = developer_message

    SYSTEM_ERROR = ("CS-00001", "system error", "")
    CATEGORY_NOT_FOUND = ("CS-00008", "category not found", "")
    USER_NOT_FOUND = ("CS-00009", "user not found", "")
    VALIDATION_ERROR = ("CS-00010", "validation error", "")


class AppException(Exception):
    def __init__(
        self,
        exc_data: AppError = None,
        code: str = None,
        error: str = None,
        developer_message: str = None,
        *args,
    ):
        if exc_data:
            self.code = exc_data.code
            self.message = exc_data.message
            self.developer_message = exc_data.developer_message

        if code:
            self.code = code
        if error:
            self.message = error
        if developer_message:
            self.developer_message = developer_message

        super().__init__(*args)


class NotFoundException(AppException):
    pass


class ValidationException(AppException):
    pass


def app_exception_handler(exception):
    http_code = 418
    if isinstance(exception, NotFoundException):
        http_code = HTTPStatus.NOT_FOUND
    elif isinstance(exception, ValidationException):
        http_code = HTTPStatus.BAD_REQUEST
    r = make_response(jsonify(exception.__dict__), http_code)
    return r


def uncaught_exception_handler(exception: Exception):
    # Get current system exception
    ex_type, ex_value, ex_traceback = sys.exc_info()

    # Extract unformatter stack traces as tuples
    trace_back = traceback.extract_tb(ex_traceback)

    # Format stacktrace
    stack_trace = []

    for trace in trace_back:
        stack_trace.append(
            "File : %s , Line : %d, Func.Name : %s, Message : %s"
            % (trace[0], trace[1], trace[2], trace[3])
        )

    logging.getLogger("main").error(f"* Uncaught exception [{exception}]: {format_exc}")
    return app_exception_handler(
        AppException(exc_data=AppError.SYSTEM_ERROR, developer_message=str(exception))
    )
