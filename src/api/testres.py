import apiflask.fields as fields
from apiflask import Schema
from flask.views import MethodView

from src.app import app
from src.core.db.database import get_session
from src.core.models import Asset


class RSchemaItem(Schema):
    ticker = fields.String()
    price = fields.Decimal()


class RSchema(Schema):
    items = fields.List(fields.Nested(RSchemaItem))


class Test(MethodView):
    @app.output(RSchema)
    def get(self):
        with get_session() as s:
            ps = s.query(Asset).all()

        return {"items": ps}
