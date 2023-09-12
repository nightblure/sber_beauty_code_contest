from contextlib import contextmanager
from pathlib import Path

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


def create_db_engine(url, stmt_timeout=5000) -> Engine:
    connect_opts = {
        "timeout": stmt_timeout,
    }

    return create_engine(
        url, connect_args=connect_opts, pool_pre_ping=True, pool_recycle=1200, echo=True
    )


ROOT = Path(__file__).parent.parent.parent.resolve()
DATABASE_URL = f"sqlite:///{ROOT}/db.db"


@contextmanager
def get_session():
    session = scoped_session(sessionmaker(autocommit=False, bind=engine))()

    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


engine = create_db_engine(DATABASE_URL)
