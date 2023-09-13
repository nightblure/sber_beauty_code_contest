from decimal import Decimal
from typing import Optional

from src.api.base_repository import BaseRepository
from src.core.db.models import User


class UserOperationsRepository(BaseRepository):
    def get_balance(self) -> Decimal:
        return self.current_user.balance

    @property
    def current_user(self) -> Optional[User]:
        with self.session() as s:
            return s.query(User).first()

    def refill_balance(self, user: User, value: Decimal) -> Decimal:
        with self.session() as s:
            locked_user = (
                s.query(User).filter(User.id == user.id).with_for_update().one()
            )
            locked_user.balance += value
            s.commit()
            return locked_user.balance
