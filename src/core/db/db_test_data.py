import os
from pathlib import Path

from src.core.db.database import engine, get_session
from src.core.db.models import Asset, Base, User


def fill_db():
    with get_session() as session:
        session.add_all(
            [
                Asset(ticker="LKOH", price=234.57),
                Asset(ticker="SBERCOIN", price=338.42356),
                Asset(ticker="ETH", price=100),
                Asset(ticker="BTC", price=250),
            ]
        )

        session.add(User(balance=1000))

        session.commit()


if __name__ == "__main__":
    db_path = Path(__file__).parent.parent.parent.parent.resolve() / "db.db"

    if Path.exists(db_path):
        os.remove(db_path)

    Base.metadata.create_all(bind=engine)
    fill_db()
