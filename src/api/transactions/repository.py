import logging

from src.api.base_repository import BaseRepository
from src.core.db.models import User, TransactionLog, OperationType
from src.domain.dto import BuyAssetDTO

logger = logging.getLogger(__name__)


class TransactionRepository(BaseRepository):
    def fill_transaction_log_by_assets(
        self, user: User, assets: list[BuyAssetDTO], operation_type: OperationType
    ) -> list[TransactionLog]:
        records = []

        for asset in assets:
            value = asset.price * asset.count
            logger.info(
                f"Add record to transaction log: "
                f"{asset.ticker}, count: {asset.count}, price: {asset.price}, total: {value}"
            )

            r = TransactionLog(
                user_id=user.id,
                asset_id=asset.id,
                operation_type=operation_type,
                value=value,
            )
            records.append(r)

        with self.session() as s:
            s.add_all(records)
            s.commit()
            return records

    def get_log_records_by_user(self, user) -> list[TransactionLog]:
        with self.session() as s:
            return (
                s.query(TransactionLog).filter(TransactionLog.user_id == user.id).all()
            )
