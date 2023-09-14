from src.api.balance.service import UserBalanceService
from src.api.transactions.service import TransactionService


class BalanceUseCases:
    def __init__(self):
        self.balance_svc = UserBalanceService()
        self.transaction_svc = TransactionService()

    def get_balance(self):
        balance = self.balance_svc.get_balance()
        assets_balance = self.transaction_svc.get_assets_balance_from_transactions()
        return balance, assets_balance

    def refill_balance(self, value):
        return self.balance_svc.refill_balance(value)
