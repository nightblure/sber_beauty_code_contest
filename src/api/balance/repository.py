from decimal import Decimal

from src.api.base_repository import BaseRepository
from src.core.db.models import User


class UserBalanceRepository(BaseRepository):
    def change_balance(self, user: User, value: Decimal) -> Decimal:
        with self.session() as s:
            locked_user = (
                s.query(User).filter(User.id == user.id).with_for_update().one()
            )
            locked_user.balance += value
            s.commit()
            return locked_user.balance
