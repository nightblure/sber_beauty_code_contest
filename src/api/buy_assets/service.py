import logging
from decimal import Decimal

from src.api.base_service import BaseService
from src.api.buy_assets.repository import BuyAssetsRepository
from src.api.utils.assets_mapping import (
    get_transactions_assets_from_mapping,
    build_db_asset_to_input_asset_mapping,
)
from src.domain.dto import TransactionAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = BuyAssetsRepository()

    def calculate_total_buy_sum(self, assets: list[TransactionAssetDTO]) -> Decimal:
        buy_sum: Decimal = Decimal(0)

        for asset in assets:
            buy_sum += asset.price * asset.count

        logger.info(f"Total buy sum: {buy_sum}")
        return buy_sum

    def get_transactions_assets(self, buy_assets, db_assets):
        db_asset_to_buy_asset = build_db_asset_to_input_asset_mapping(
            buy_assets, db_assets
        )
        assets = get_transactions_assets_from_mapping(db_asset_to_buy_asset)
        return assets
