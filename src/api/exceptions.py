from src.core.exceptions import ApplicationError


class InsufficientFundsToBuyAssetError(ApplicationError):
    status_code = 400

    def __init__(self, asset_ticker):
        self.message = f"Insufficient funds to buy asset '{asset_ticker}'"


class AssetNotFoundError(ApplicationError):
    status_code = 404

    def __init__(self, asset_ticker):
        self.message = f"Ticker '{asset_ticker}' does not exists"


class InsufficientAssetFundsToSellError(ApplicationError):
    status_code = 400

    def __init__(self, asset_ticker):
        self.message = f"Insufficient asset funds to sell for '{asset_ticker}'"


class AssetNotFoundInPortfolioError(ApplicationError):
    status_code = 400

    def __init__(self, asset_ticker):
        self.message = f"Asset '{asset_ticker}' not found in portfolio"
