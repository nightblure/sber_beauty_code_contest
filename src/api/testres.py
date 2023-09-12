from flask.views import MethodView

from src.core.database import get_session
from src.core.models import Asset


class Test(MethodView):
    def get(self):
        with get_session() as s:
            ps = s.query(Asset).all()
            s = ""
            for p in ps:
                s += f"<p>Hello, {p.ticker} {p.price}!  </p> <br>"
        return s
