import logging

from src.api.assets.service import AssetsService
from src.api.balance.service import UserBalanceService
from src.api.buy_assets.service import BuyAssetsService
from src.api.exceptions import InsufficientFundsToBuyAssetError, AssetNotFoundError
from src.api.transactions.service import TransactionService
from src.core.db.enums import OperationType
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsUseCases:
    def __init__(self):
        self.balance_svc = UserBalanceService()
        self.buy_assets_svc = BuyAssetsService()
        self.assets_svc = AssetsService()
        self.transaction_svc = TransactionService()

    def buy_assets(self, buy_assets: list[BuyAssetDTO]):
        user = self.buy_assets_svc.repository.current_user

        # check input assets existing
        is_assets_exists, not_found_ticker = self.assets_svc.is_assets_exists(
            buy_assets
        )

        if is_assets_exists is False:
            raise AssetNotFoundError(not_found_ticker)

        # check that user balance enough for buy operation
        buy_assets_with_prices = self.assets_svc.fill_assets_prices(buy_assets)

        for buy_asset in buy_assets_with_prices:
            if user.balance < buy_asset.price * buy_asset.count:
                raise InsufficientFundsToBuyAssetError(buy_asset.ticker)

        # fill the transaction log and charge off funds from the user balance
        self.transaction_svc.fill_transaction_log(
            buy_assets_with_prices, user, OperationType.buy
        )
        buy_sum = self.buy_assets_svc.calculate_total_buy_sum(buy_assets_with_prices)
        return self.balance_svc.charge_off_from_balance(buy_sum)
