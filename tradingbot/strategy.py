import pandas as pd
from collections import deque
from typing import Deque, Dict


class SMACrossStrategy:
    """Simple moving average crossover strategy."""

    def __init__(self, short_window: int = 20, long_window: int = 50):
        self.short_window = short_window
        self.long_window = long_window
        self.history: Dict[str, Deque[float]] = {}

    def on_price(self, symbol: str, price: float) -> str:
        q = self.history.setdefault(symbol, deque(maxlen=self.long_window))
        q.append(price)
        if len(q) < self.long_window:
            return "HOLD"

        series = pd.Series(q)
        short_sma = series.tail(self.short_window).mean()
        long_sma = series.mean()
        if short_sma > long_sma:
            return "BUY"
        elif short_sma < long_sma:
            return "SELL"
        return "HOLD"
