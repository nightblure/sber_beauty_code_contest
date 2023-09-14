from src.core.exceptions import ApplicationError


class InsufficientFundsError(ApplicationError):
    status_code = 400
    message = "Insufficient funds"


class AssetNotFoundError(ApplicationError):
    status_code = 404

    def __init__(self, asset_ticker):
        self.message = f"Ticker '{asset_ticker}' does not exists"


class InsufficientAssetFundsError(ApplicationError):
    status_code = 400

    def __init__(self, asset_ticker):
        self.message = f"Insufficient asset funds for '{asset_ticker}'"


class AssetNotFoundInPortfolioError(ApplicationError):
    status_code = 400

    def __init__(self, asset_ticker):
        self.message = f"Asset '{asset_ticker}' not found in portfolio"
