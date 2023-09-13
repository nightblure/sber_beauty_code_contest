from src.api.user_operations.schemas.buy_assets import (
    BuyAssetsSuccessSchema,
    BuyAssetsArgs,
)
from src.api.user_operations.schemas.refill_balance import (
    RefillBalanceArgs,
    RefillBalanceSchema,
)
from src.api.user_operations.schemas.user_balance import BalanceSchema
from src.app import app
from src.domain.dto import AssetDTO
from src.domain.use_cases.user import UserUseCases


@app.output(BalanceSchema)
def get_user_balance():
    uc = UserUseCases()
    return {"balance": uc.get_balance()}


@app.input(BuyAssetsArgs, location="json")
@app.output(BuyAssetsSuccessSchema)
def buy_assets(json_data):
    uc = UserUseCases()
    assets = [AssetDTO(**asset_data) for asset_data in json_data["assets"]]
    uc.buy_assets(assets)
    return {"body": json_data, "success": True}


@app.input(RefillBalanceArgs, location="json")
@app.output(RefillBalanceSchema)
def refill_balance(json_data):
    uc = UserUseCases()
    value = json_data["value"]
    new_balance = uc.refill_balance(value)
    return {"value": value, "new_balance": new_balance}
