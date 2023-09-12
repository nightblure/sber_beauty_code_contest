from src.core.models import User
from src.api.base_service import BaseService


class OperationService(BaseService):
    def get_balance(self):
        with self.session as s:
            u = s.query(User).first()
        return {"sfd": u.balance}
