from decimal import Decimal

from src.api.assets.service import AssetsService
from src.api.balance.repository import UserBalanceRepository
from src.api.base_service import BaseService


class UserBalanceService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = UserBalanceRepository()
        self.assets_svc = AssetsService()

    def get_balance(self) -> Decimal:
        return self.repository.current_user.balance

    def refill_balance(self, value: Decimal) -> Decimal:
        return self.repository.change_balance(self.repository.current_user, value)

    def charge_off_from_balance(self, value: Decimal) -> Decimal:
        return self.repository.change_balance(self.repository.current_user, -value)
