from src.api.base_service import BaseService
from src.api.common.repository import CommonRepository


class CommonService(BaseService):
    def __init__(self):
        super().__init__()
        self.repository = CommonRepository()

    def get_assets(self):
        return self.repository.get_assets()
