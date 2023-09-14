import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class BuyAssetDTO:
    ticker: str
    count: Decimal

    def __hash__(self):
        return hash(self.ticker)


@dataclasses.dataclass
class SellAssetDTO:
    ticker: str
    count: Decimal


@dataclasses.dataclass
class AssetBalanceDTO:
    ticker: str
    total: Decimal


@dataclasses.dataclass
class TransactionAssetDTO:
    ticker: str
    price: Decimal
    count: Decimal
    id: int
