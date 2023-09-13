from decimal import Decimal

from src.api.base_service import BaseService
from src.api.user_operations.repository import UserOperationsRepository


class UserOperationsService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = UserOperationsRepository()

    def get_balance(self) -> Decimal:
        user = self.repository.current_user
        return user.balance

    def refill_balance(self, value) -> Decimal:
        user = self.repository.current_user
        return self.repository.refill_balance(user, value)
