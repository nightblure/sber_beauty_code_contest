import logging

from apiflask import APIFlask

from src.core.exception_handlers import (
    uncaught_exception_handler,
    default_exception_handler,
)
from src.core.exceptions import ApplicationError

logger = logging.getLogger("main")
logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s] [%(name)s] [%(levelname)s] > [*] %(message)s",
)


def create_app():
    app = APIFlask(__name__)
    # if not config.DEBUG:
    app.register_error_handler(ApplicationError, uncaught_exception_handler)
    app.register_error_handler(Exception, default_exception_handler)
    return app


app = create_app()
