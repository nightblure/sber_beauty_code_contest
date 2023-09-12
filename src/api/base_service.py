from src.core.db.database import get_session


class BaseService:
    def __init__(self):
        self.session = get_session()
