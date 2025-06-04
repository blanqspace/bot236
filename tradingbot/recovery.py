import json
from typing import Dict
from tradingbot.config import RECOVERY_FILE
from tradingbot.state import BotState, SymbolState


def save_state(state: BotState):
    data = {sym: vars(s) for sym, s in state.symbols.items()}
    with open(RECOVERY_FILE, "w") as fh:
        json.dump(data, fh)


def load_state(symbols) -> BotState:
    try:
        with open(RECOVERY_FILE) as fh:
            raw = json.load(fh)
    except FileNotFoundError:
        raw = {}
    state = BotState()
    for sym in symbols:
        info = raw.get(sym, {})
        state.symbols[sym] = SymbolState(**info)
    return state
