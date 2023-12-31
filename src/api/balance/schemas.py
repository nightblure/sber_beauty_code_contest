import apiflask.fields as fields
from apiflask import Schema
from marshmallow import validates, ValidationError


class RefillBalanceArgs(Schema):
    value = fields.Decimal()

    @validates("value")
    def validate_positive_value(self, value):
        if value <= 0:
            raise ValidationError("Value must be positive")


class RefillBalanceSchema(Schema):
    value = fields.Decimal()
    current_balance = fields.Decimal()


class AssetBalance(Schema):
    ticker = fields.String()
    total = fields.Decimal()


class BalanceSchema(Schema):
    balance = fields.Decimal()
    assets_balance = fields.List(fields.Nested(AssetBalance))
