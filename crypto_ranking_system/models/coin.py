from dataclasses import dataclass

@dataclass
class Coin:
    coin_id: int
    name: str
    symbol: str
    rank: int
    price: float
    market_cap: float
    volume_24h: float