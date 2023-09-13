import logging
import sys
import traceback


from src.core.exceptions import ApplicationError

logger = logging.getLogger(__name__)


def uncaught_exception_handler(exception: ApplicationError):
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

    logger.error(
        f"Uncaught exception: {exception.__class__.__name__} ({exception.message})"
    )
    return {"message": exception.message}, exception.status_code


def default_exception_handler(error):
    logger.exception(error)
    return {"message": "Internal Error"}, 500
