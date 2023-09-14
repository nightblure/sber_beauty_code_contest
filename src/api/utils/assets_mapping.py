from src.core.db.models import Asset
from src.domain.dto import SellAssetDTO, BuyAssetDTO, TransactionAssetDTO


def build_db_asset_to_input_asset_mapping(
    input_assets: list[SellAssetDTO | BuyAssetDTO], db_assets: list[Asset]
) -> dict[Asset, SellAssetDTO | BuyAssetDTO]:
    ticker_to_input_asset = {a.ticker: a for a in input_assets}

    mapping = {}

    for db_asset in db_assets:
        input_asset = ticker_to_input_asset.get(db_asset.ticker)
        mapping[db_asset] = input_asset

    return mapping


def get_transactions_assets_from_mapping(
    db_asset_to_input_asset,
) -> list[TransactionAssetDTO]:
    assets = []
    for db_asset in db_asset_to_input_asset:
        buy_asset = db_asset_to_input_asset[db_asset]
        assets.append(
            TransactionAssetDTO(
                id=db_asset.id,
                ticker=db_asset.ticker,
                price=db_asset.price,
                count=buy_asset.count,
            )
        )
    return assets
