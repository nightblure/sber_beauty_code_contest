import logging

from src.api.assets.service import AssetsService
from src.api.balance.exceptions import InsufficientFundsError, AssetNotFoundError
from src.api.balance.service import UserBalanceService
from src.api.buy_assets.service import BuyAssetsService
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class BuyAssetsUseCases:
    def __init__(self):
        self.operations_svc = UserBalanceService()
        self.buy_assets_svc = BuyAssetsService()
        self.assets_svc = AssetsService()

    def buy_assets(self, buy_assets: list[BuyAssetDTO]):
        user = self.operations_svc.repository.current_user

        tickers = [asset.ticker for asset in buy_assets]
        db_assets = self.assets_svc.get_assets(tickers)
        db_ticker_to_asset = {asset.ticker: asset for asset in db_assets}

        for asset in buy_assets:
            if asset.ticker not in db_ticker_to_asset:
                raise AssetNotFoundError(asset.ticker)

        buy_assets_with_prices = self.buy_assets_svc.fill_buy_assets_prices(buy_assets)

        buy_sum = self.buy_assets_svc.calculate_total_buy_sum(buy_assets_with_prices)
        user_balance = user.balance

        if user_balance < buy_sum:
            raise InsufficientFundsError()

        self.buy_assets_svc.fill_transaction_log(buy_assets_with_prices, user)
        return self.operations_svc.charge_off_from_balance(buy_sum)
