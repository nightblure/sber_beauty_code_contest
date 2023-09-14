from src.api.sell_assets.schemas import SellAssetsArgs, SellAssetsSchema
from src.app import app
from src.domain.dto import SellAssetDTO
from src.domain.use_cases.sell_assets import SellAssetsUseCases


@app.input(SellAssetsArgs, location="json")
@app.output(SellAssetsSchema)
def sell_assets(json_data):
    uc = SellAssetsUseCases()
    assets = [SellAssetDTO(**asset_data) for asset_data in json_data["assets"]]
    current_balance = uc.sell_assets(assets)
    return {"body": json_data, "current_balance": current_balance, "success": True}
