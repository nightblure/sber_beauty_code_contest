from flask import Blueprint

from src.api import testres

app_blueprint = Blueprint("app_blueprint", __name__)


def register_urls(app):
    app.register_blueprint(app_blueprint, url_prefix="/api")


test = testres.Test.as_view("Test")
app_blueprint.add_url_rule("", view_func=test)
