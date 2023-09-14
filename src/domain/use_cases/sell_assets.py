import logging

from src.api.assets.service import AssetsService
from src.api.balance.service import UserBalanceService
from src.api.exceptions import (
    InsufficientAssetFundsToSellError,
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
        self.balance_svc = UserBalanceService()
        self.assets_svc = AssetsService()
        self.transaction_svc = TransactionService()
        self.sell_assets_svc = SellAssetsService()

    def sell_assets(self, sell_assets: list[SellAssetDTO]):
        user = self.balance_svc.repository.current_user

        # check input assets existing
        is_assets_exists, not_found_ticker = self.assets_svc.is_assets_exists(
            sell_assets
        )

        if is_assets_exists is False:
            raise AssetNotFoundError(not_found_ticker)

        # check that user have enough asset balance to sell asset
        db_assets_balance = self.transaction_svc.get_assets_balance_from_transactions()
        db_asset_to_balance = {a.ticker: a.total for a in db_assets_balance}

        tickers = [a.ticker for a in sell_assets]
        db_assets = self.assets_svc.get_assets(tickers)

        assets = self.sell_assets_svc.get_transactions_assets(sell_assets, db_assets)

        for sell_asset in assets:
            sell_sum = sell_asset.count * sell_asset.price
            db_asset_balance = db_asset_to_balance.get(sell_asset.ticker)

            if db_asset_balance is None:
                raise AssetNotFoundInPortfolioError(sell_asset.ticker)

            if db_asset_balance < sell_sum:
                raise InsufficientAssetFundsToSellError(sell_asset.ticker)

        # fill the transaction log and refill user balance
        self.transaction_svc.fill_transaction_log(assets, user, OperationType.sell)

        sell_sum = self.sell_assets_svc.calculate_total_sell_sum(assets)
        return self.balance_svc.refill_balance(sell_sum)
