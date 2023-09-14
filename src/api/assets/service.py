from typing import Optional

from src.api.assets.repository import AssetRepository
from src.api.base_service import BaseService


class AssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = AssetRepository()

    def get_assets(self, tickers: list[str] = None):
        return self.repository.get_assets(tickers)

    def is_assets_exists(self, assets) -> tuple[bool, Optional[str]]:
        tickers = [asset.ticker for asset in assets]
        db_assets = self.get_assets(tickers)
        ticker_to_db_asset = {asset.ticker: asset for asset in db_assets}

        for asset in assets:
            if asset.ticker not in ticker_to_db_asset:
                return False, asset.ticker

        return True, None
