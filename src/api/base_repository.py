from typing import Optional

from src.core.db.database import get_session
from src.core.db.models import User


class BaseRepository:
    def __init__(self):
        self.session = get_session  # NO NEED TO CALL THIS FUNCTION HERE !!!

    @property
    def current_user(self) -> Optional[User]:
        with self.session() as s:
            return s.query(User).first()
