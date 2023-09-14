import apiflask.fields as fields
from apiflask import Schema


class AssetSchema(Schema):
    ticker = fields.String()
    price = fields.Decimal()


class AssetsSchema(Schema):
    assets = fields.List(fields.Nested(AssetSchema))
