from src.api.balance.schemas import (
    RefillBalanceArgs,
    RefillBalanceSchema,
    BalanceSchema,
)
from src.app import app
from src.domain.use_cases.balance import BalanceUseCases


@app.output(BalanceSchema)
def get_user_balance():
    uc = BalanceUseCases()
    return {"balance": uc.get_balance()}


@app.input(RefillBalanceArgs, location="json")
@app.output(RefillBalanceSchema)
def refill_balance(json_data):
    uc = BalanceUseCases()
    value = json_data["value"]
    current_balance = uc.refill_balance(value)
    return {"value": value, "current_balance": current_balance}
