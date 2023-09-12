from src.domain.use_cases import UserUseCases


def get_user_balance():
    uc = UserUseCases()
    return uc.get_balance()
