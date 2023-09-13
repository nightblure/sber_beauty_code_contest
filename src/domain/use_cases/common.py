from src.api.common.service import CommonService


class CommonUseCases:
    def __init__(self):
        self.common_svc = CommonService()

    def get_assets(self):
        return self.common_svc.get_assets()
