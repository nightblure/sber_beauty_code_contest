from contextlib import contextmanager
from pathlib import Path

from sqlalchemy.engine import Engine, create_engine
from sqlalchemy.orm import sessionmaker, Session, scoped_session


def create_db_engine(url, stmt_timeout=5000) -> Engine:
    connect_opts = {
        "timeout": stmt_timeout,
    }

    return create_engine(
        url,
        connect_args=connect_opts,
        pool_pre_ping=True,
        pool_recycle=1200,
        echo=False,
        future=True,
    )


ROOT = Path(__file__).parent.parent.parent.parent.resolve()
DATABASE_URL = f"sqlite:///{ROOT}/db.db"

engine = create_db_engine(DATABASE_URL)
_Session = scoped_session(sessionmaker(autocommit=False, bind=engine))


@contextmanager
def get_session() -> Session:
    session = _Session()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
