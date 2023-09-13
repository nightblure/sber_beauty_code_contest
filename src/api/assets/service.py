from src.api.base_service import BaseService
from src.api.assets.repository import AssetRepository


class AssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = AssetRepository()

    def get_assets(self, tickers: list[str] = None):
        return self.repository.get_assets(tickers)
