import apiflask.fields as fields
from apiflask import Schema


class BalanceSchema(Schema):
    balance = fields.Decimal()
