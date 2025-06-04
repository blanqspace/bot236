from typing import Dict
from .utils.logging import setup_logger

logger = setup_logger()


class OrderManager:
    """Handles order submission and prevents duplicates."""

    def __init__(self):
        self.last_action: Dict[str, str] = {}

    def submit(self, symbol: str, action: str, qty: int):
        key = f"{symbol}:{action}"
        if self.last_action.get(symbol) == key:
            logger.info("Duplicate order ignored: %s", key)
            return
        self.last_action[symbol] = key
        logger.info("Order %s %s %s", action, qty, symbol)
