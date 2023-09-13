import dataclasses


@dataclasses.dataclass
class AssetDTO:
    ticker: str
    count: float
