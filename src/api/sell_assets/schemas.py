import apiflask.fields as fields
from apiflask import Schema
from apiflask.validators import Length
from marshmallow import validates, ValidationError


class SellAssetArg(Schema):
    ticker = fields.String()
    count = fields.Decimal()

    @validates("count")
    def validate_positive_count(self, count):
        if count <= 0:
            raise ValidationError("Count must be positive")


class SellAssetsArgs(Schema):
    assets = fields.List(fields.Nested(SellAssetArg), validate=Length(min=1))

    @validates("assets")
    def validate_unique_assets_ticker(self, assets):
        if len({asset["ticker"] for asset in assets}) != len(assets):
            raise ValidationError("Tickers must be unique")


class SellAssetsSchema(Schema):
    body = fields.Nested(SellAssetsArgs)
    current_balance = fields.Decimal()
    success = fields.Boolean()
