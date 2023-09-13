from src.api.base_repository import BaseRepository
from src.core.db.models import Asset


class AssetRepository(BaseRepository):
    def get_assets(self, tickers: list[str] = None) -> list[Asset]:
        with self.session() as s:
            if tickers is None:
                assets = s.query(Asset).all()
            else:
                assets = s.query(Asset).filter(Asset.ticker.in_(tickers)).all()

            return assets
