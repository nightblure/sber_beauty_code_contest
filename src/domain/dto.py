import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class BuyAssetDTO:
    ticker: str
    count: Decimal
    price: Decimal = None
    id: int = None


@dataclasses.dataclass
class SellAssetDTO:
    ticker: str
    count: Decimal
    price: Decimal = None
    id: int = None


@dataclasses.dataclass
class AssetBalanceDTO:
    ticker: str
    total: Decimal


@dataclasses.dataclass
class AssetDTO:
    ticker: str
    price: Decimal
    count: Decimal
    id: int
