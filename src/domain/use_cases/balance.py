from src.api.balance.service import UserBalanceService


class BalanceUseCases:
    def __init__(self):
        self.operations_svc = UserBalanceService()

    def get_balance(self):
        return self.operations_svc.get_balance()

    def refill_balance(self, value):
        return self.operations_svc.refill_balance(value)
