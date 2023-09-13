from src.api.buy_assets.schemas import BuyAssetsArgs, BuyAssetsSuccessSchema
from src.app import app
from src.domain.dto import BuyAssetDTO
from src.domain.use_cases.buy_assets import BuyAssetsUseCases


@app.input(BuyAssetsArgs, location="json")
@app.output(BuyAssetsSuccessSchema)
def buy_assets(json_data):
    uc = BuyAssetsUseCases()
    assets = [BuyAssetDTO(**asset_data) for asset_data in json_data["assets"]]
    current_balance = uc.buy_assets(assets)
    return {"body": json_data, "current_balance": current_balance, "success": True}
