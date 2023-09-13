from src.core.db.database import get_session


class BaseRepository:
    def __init__(self):
        self.session = get_session  # DON'T CALL THIS FUNCTION !!!
