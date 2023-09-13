from src.core.db.database import engine, get_session
from src.core.db.models import Asset, Base, User

Base.metadata.create_all(bind=engine)


def fill_db():
    with get_session() as session:
        session.add_all(
            [
                Asset(ticker="LKOH", price=234.57),
                Asset(ticker="SBERCOIN", price=338.42356),
            ]
        )

        session.add(User(balance=1000))

        session.commit()


if __name__ == "__main__":
    fill_db()
