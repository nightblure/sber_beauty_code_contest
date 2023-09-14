import logging
from decimal import Decimal

from src.api.assets.service import AssetsService
from src.api.base_service import BaseService
from src.api.sell_assets.repository import SellAssetsRepository
from src.api.utils.assets_mapping import (
    build_db_asset_to_input_asset_mapping,
    get_transactions_assets_from_mapping,
)
from src.domain.dto import TransactionAssetDTO

logger = logging.getLogger(__name__)


class SellAssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = SellAssetsRepository()
        self.assets_svc = AssetsService()

    def calculate_total_sell_sum(self, assets: list[TransactionAssetDTO]) -> Decimal:
        sell_sum: Decimal = Decimal(0)

        for asset in assets:
            sell_sum += asset.price * asset.count

        logger.info(f"Total sell sum: {sell_sum}")
        return sell_sum

    def get_transactions_assets(self, buy_assets, db_assets):
        db_asset_to_buy_asset = build_db_asset_to_input_asset_mapping(
            buy_assets, db_assets
        )
        assets = get_transactions_assets_from_mapping(db_asset_to_buy_asset)
        return assets
