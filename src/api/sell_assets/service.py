import logging
from decimal import Decimal

from src.api.assets.service import AssetsService
from src.api.base_service import BaseService
from src.api.sell_assets.repository import SellAssetsRepository
from src.domain.dto import SellAssetDTO

logger = logging.getLogger(__name__)


class SellAssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = SellAssetsRepository()
        self.assets_svc = AssetsService()

    def calculate_total_sell_sum(self, assets: list[SellAssetDTO]) -> Decimal:
        sell_sum: Decimal = Decimal(0)

        for asset in assets:
            sell_sum += asset.price * asset.count

        logger.info(f"Total sell sum: {sell_sum}")
        return sell_sum
