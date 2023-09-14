from src.api.base_repository import BaseRepository
from src.core.db.models import User, TransactionLog, OperationType
from src.domain.dto import BuyAssetDTO


class SellAssetsRepository(BaseRepository):
    def fill_transaction_log_by_assets(
        self, user: User, assets: list[BuyAssetDTO], operation_type: OperationType
    ) -> list[TransactionLog]:
        records = []

        for asset in assets:
            value = asset.price * asset.count

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
