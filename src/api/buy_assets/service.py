import logging
from decimal import Decimal

from src.api.base_service import BaseService
from src.api.buy_assets.repository import BuyAssetsRepository
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = BuyAssetsRepository()

    def calculate_total_buy_sum(self, assets: list[BuyAssetDTO]) -> Decimal:
        buy_sum: Decimal = Decimal(0)

        for asset in assets:
            buy_sum += asset.price * asset.count

        logger.info(f"Total buy sum: {buy_sum}")
        return buy_sum
