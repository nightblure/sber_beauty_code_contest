import logging
from decimal import Decimal

from src.api.assets.service import AssetsService
from src.api.base_service import BaseService
from src.api.buy_assets.repository import BuyAssetsRepository
from src.core.db.models import OperationType
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = BuyAssetsRepository()
        self.assets_svc = AssetsService()

    def fill_transaction_log(self, assets: list[BuyAssetDTO], user):
        self.repository.fill_transaction_log_by_assets(
            user=user,
            assets=assets,
            operation_type=OperationType.buy,
        )

    def calculate_total_buy_sum(self, assets: list[BuyAssetDTO]) -> Decimal:
        buy_sum: Decimal = Decimal(0)

        for asset in assets:
            buy_sum += asset.price * asset.count

        logger.info(f"Total buy sum: {buy_sum}")
        return buy_sum

    def fill_buy_assets_prices(self, buy_assets):
        buy_assets_tickers = [asset.ticker for asset in buy_assets]
        db_assets = self.assets_svc.get_assets(buy_assets_tickers)
        ticker_to_buy_asset = {asset.ticker: asset for asset in buy_assets}

        assets = []

        for asset in db_assets:
            buy_count = ticker_to_buy_asset[asset.ticker].count
            dto = BuyAssetDTO(
                ticker=asset.ticker, count=buy_count, price=asset.price, id=asset.id
            )
            assets.append(dto)

        return assets
