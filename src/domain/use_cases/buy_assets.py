import logging

from src.api.assets.service import AssetsService
from src.api.exceptions import InsufficientFundsError, AssetNotFoundError
from src.api.balance.service import UserBalanceService
from src.api.buy_assets.service import BuyAssetsService
from src.api.transactions.service import TransactionService
from src.core.db.enums import OperationType
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsUseCases:
    def __init__(self):
        self.operations_svc = UserBalanceService()
        self.buy_assets_svc = BuyAssetsService()
        self.assets_svc = AssetsService()
        self.transaction_svc = TransactionService()

    def buy_assets(self, buy_assets: list[BuyAssetDTO]):
        user = self.operations_svc.repository.current_user

        # check input assets existing
        tickers = [asset.ticker for asset in buy_assets]
        db_assets = self.assets_svc.get_assets(tickers)
        ticker_to_db_asset = {asset.ticker: asset for asset in db_assets}

        for asset in buy_assets:
            if asset.ticker not in ticker_to_db_asset:
                raise AssetNotFoundError(asset.ticker)

        # check that user balance enough for buy operation
        buy_assets_with_prices = self.assets_svc.fill_assets_prices(buy_assets)
        buy_sum = self.buy_assets_svc.calculate_total_buy_sum(buy_assets_with_prices)

        if user.balance < buy_sum:
            raise InsufficientFundsError()

        # fill the transaction log and charge off funds from the user balance
        self.transaction_svc.fill_transaction_log(
            buy_assets_with_prices, user, OperationType.buy
        )
        return self.operations_svc.charge_off_from_balance(buy_sum)
