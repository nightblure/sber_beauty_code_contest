from src.api.user_operations.service import UserOperationsService
from src.domain.dto import AssetDTO


class UserUseCases:
    def __init__(self):
        self.operations_svc = UserOperationsService()

    def get_balance(self):
        return self.operations_svc.get_balance()

    def refill_balance(self, value):
        return self.operations_svc.refill_balance(value)

    def buy_assets(self, assets: list[AssetDTO]):
        pass
