import random
from typing import Dict


class MarketData:
    """Simulated market data provider."""

    def __init__(self, symbols):
        self.symbols = symbols
        self.prices: Dict[str, float] = {s: 100.0 for s in symbols}

    def update(self):
        for s in self.symbols:
            change = random.uniform(-1, 1)
            self.prices[s] = max(1, self.prices[s] + change)

    def get_price(self, symbol: str) -> float:
        return self.prices[symbol]
