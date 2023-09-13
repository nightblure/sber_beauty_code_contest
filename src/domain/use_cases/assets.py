from src.api.assets.service import AssetsService


class AssetsUseCases:
    def __init__(self):
        self.assets_svc = AssetsService()

    def get_assets(self, tickers: list[str] = None):
        return self.assets_svc.get_assets(tickers)
