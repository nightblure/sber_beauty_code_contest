from apiflask import APIBlueprint

from src.api.common.views import get_assets
from src.api.user_operations.views import get_user_balance, buy_assets, refill_balance


def register_urls(app):
    app_blueprint.register_blueprint(user_blueprint, url_prefix="user")
    app.register_blueprint(app_blueprint, url_prefix="/api")


app_blueprint = APIBlueprint("common", __name__)
user_blueprint = APIBlueprint("user", __name__)


app_blueprint.add_url_rule("assets", view_func=get_assets, methods=["GET"])

user_blueprint.add_url_rule("balance", view_func=get_user_balance, methods=["GET"])
user_blueprint.add_url_rule("buy-assets", view_func=buy_assets, methods=["POST"])
user_blueprint.add_url_rule(
    "refill-balance", view_func=refill_balance, methods=["POST"]
)
