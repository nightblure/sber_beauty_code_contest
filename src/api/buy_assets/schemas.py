import apiflask.fields as fields
from apiflask import Schema
from apiflask.validators import Length
from marshmallow import validates, ValidationError


class BuyAssetArg(Schema):
    ticker = fields.String()
    count = fields.Decimal()

    @validates("count")
    def validate_positive_count(self, count):
        if count <= 0:
            raise ValidationError("Count must be positive")


class BuyAssetsArgs(Schema):
    assets = fields.List(fields.Nested(BuyAssetArg), validate=Length(min=1))

    @validates("assets")
    def validate_unique_assets_ticker(self, assets):
        if len({asset["ticker"] for asset in assets}) != len(assets):
            raise ValidationError("Tickers must be unique")


class BuyAssetsSuccessSchema(Schema):
    body = fields.Nested(BuyAssetsArgs)
    current_balance = fields.Decimal()
    success = fields.Boolean()
