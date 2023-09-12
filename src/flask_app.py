from flask import Flask

from src.api.routes import register_urls

# from src.core.exception_handlers import uncaught_exception_handler


def create_app():
    app = Flask(__name__)
    register_urls(app)
    # if not config.DEBUG:
    #     app.errorhandler(Exception)(uncaught_exception_handler)
    return app


app = create_app()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5020)
