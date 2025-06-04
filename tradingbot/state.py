from dataclasses import dataclass, field
from typing import Dict


@dataclass
class SymbolState:
    position: int = 0
    paused: bool = False


@dataclass
class BotState:
    symbols: Dict[str, SymbolState] = field(default_factory=dict)

    def ensure_symbol(self, symbol: str) -> SymbolState:
        return self.symbols.setdefault(symbol, SymbolState())
