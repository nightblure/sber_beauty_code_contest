from apiflask import APIBlueprint

from src.api.views import get_user_balance
from src.api import testres


def register_urls(app):
    app.register_blueprint(app_blueprint, url_prefix="/api")


app_blueprint = APIBlueprint("sber contest", __name__)
test = testres.Test.as_view("Test")

app_blueprint.add_url_rule("", view_func=test)


app_blueprint.add_url_rule("user-balance", view_func=get_user_balance)
