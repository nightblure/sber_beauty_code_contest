from apiflask import APIFlask

# from src.core.exception_handlers import uncaught_exception_handler


def create_app():
    app = APIFlask(__name__)
    # if not config.DEBUG:
    #     app.errorhandler(Exception)(uncaught_exception_handler)
    return app


app = create_app()
