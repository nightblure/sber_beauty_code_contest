import logging
from collections import defaultdict
from decimal import Decimal

from src.api.base_service import BaseService
from src.api.transactions.repository import TransactionRepository
from src.core.db.models import OperationType
from src.domain.dto import BuyAssetDTO, AssetBalanceDTO

logger = logging.getLogger(__name__)


class TransactionService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = TransactionRepository()

    def fill_transaction_log(
        self, assets: list[BuyAssetDTO], user, operation_type: OperationType
    ):
        self.repository.fill_transaction_log_by_assets(
            user=user,
            assets=assets,
            operation_type=operation_type,
        )

    def get_assets_balance_from_transactions(self) -> list[AssetBalanceDTO]:
        logs = self.repository.get_log_records_by_user(self.repository.current_user)

        records = []
        ticker_to_total_balance = defaultdict(Decimal)

        for log in logs:
            if log.operation_type == OperationType.buy:
                ticker_to_total_balance[log.asset.ticker] += log.value
            else:
                ticker_to_total_balance[log.asset.ticker] -= log.value

        for ticker in ticker_to_total_balance:
            total = ticker_to_total_balance[ticker]
            records.append(AssetBalanceDTO(ticker=ticker, total=total))

        return records
