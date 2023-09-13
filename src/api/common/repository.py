from typing import Type

from src.api.base_repository import BaseRepository
from src.core.db.models import Asset


class CommonRepository(BaseRepository):
    def get_assets(self) -> list[Type[Asset]]:
        with self.session() as s:
            return s.query(Asset).all()
