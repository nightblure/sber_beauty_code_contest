from src.api.assets.schemas import AssetsSchema
from src.app import app
from src.domain.use_cases.assets import AssetsUseCases


@app.output(AssetsSchema)
def get_assets():
    uc = AssetsUseCases()
    return {"items": uc.get_assets()}
