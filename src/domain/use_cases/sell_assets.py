import logging

from src.api.assets.service import AssetsService
from src.api.balance.service import UserBalanceService
from src.api.exceptions import (
    InsufficientAssetFundsError,
    AssetNotFoundError,
    AssetNotFoundInPortfolioError,
)
from src.api.sell_assets.service import SellAssetsService
from src.api.transactions.service import TransactionService
from src.core.db.enums import OperationType
from src.domain.dto import SellAssetDTO

logger = logging.getLogger(__name__)


class SellAssetsUseCases:
    def __init__(self):
        self.operations_svc = UserBalanceService()
        self.assets_svc = AssetsService()
        self.transaction_svc = TransactionService()
        self.sell_assets_svc = SellAssetsService()

    def sell_assets(self, sell_assets: list[SellAssetDTO]):
        user = self.operations_svc.repository.current_user

        # check input assets existing
        tickers = [asset.ticker for asset in sell_assets]
        db_assets = self.assets_svc.get_assets(tickers)
        ticker_to_db_asset = {asset.ticker: asset for asset in db_assets}

        for asset in sell_assets:
            if asset.ticker not in ticker_to_db_asset:
                raise AssetNotFoundError(asset.ticker)

        # check that user have enough asset balance to sell asset
        db_assets_balance = self.transaction_svc.get_assets_balance_from_transactions()
        db_asset_to_balance = {a.ticker: a.total for a in db_assets_balance}

        sell_assets_with_prices = self.assets_svc.fill_assets_prices(sell_assets)

        for sell_asset in sell_assets_with_prices:
            sell_sum = sell_asset.count * sell_asset.price
            db_asset_balance = db_asset_to_balance.get(sell_asset.ticker)

            if db_asset_balance is None:
                raise AssetNotFoundInPortfolioError(sell_asset.ticker)

            if db_asset_balance < sell_sum:
                raise InsufficientAssetFundsError(sell_asset.ticker)

        # fill the transaction log and refill user balance
        self.transaction_svc.fill_transaction_log(
            sell_assets_with_prices, user, OperationType.sell
        )
        sell_sum = self.sell_assets_svc.calculate_total_sell_sum(
            sell_assets_with_prices
        )
        return self.operations_svc.refill_balance(sell_sum)
