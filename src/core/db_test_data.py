from src.core.database import engine, get_session
from src.core.models import Asset, Base


def fill_db():
    Base.metadata.create_all(bind=engine)

    with get_session() as s:
        s.bulk_save_objects(
            [Asset(ticker="asdad", price=20), Asset(ticker="dddd", price=20)]
        )
        s.commit()


fill_db()
