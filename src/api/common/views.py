from src.api.common.schemas import AssetsSchema
from src.app import app
from src.domain.use_cases.common import CommonUseCases


@app.output(AssetsSchema)
def get_assets():
    uc = CommonUseCases()
    return {"items": uc.get_assets()}
