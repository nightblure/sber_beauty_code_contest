from src.api.services.operations import OperationService


class UserUseCases:
    def get_balance(self):
        return OperationService().get_balance()
