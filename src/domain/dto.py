import dataclasses
from decimal import Decimal


@dataclasses.dataclass
class BuyAssetDTO:
    ticker: str
    count: Decimal
    price: Decimal = None
    id: int = None
