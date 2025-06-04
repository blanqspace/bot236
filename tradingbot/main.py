import time
from typing import Dict

"""Entry point for the trading bot."""

# Allow running as a script by adding the parent directory to ``sys.path``.
if __package__ is None or __package__ == "":  # pragma: no cover - runtime safety
    import sys
    from pathlib import Path

    sys.path.append(str(Path(__file__).resolve().parent.parent))

from tradingbot.config import SYMBOLS
from tradingbot.market import MarketData
from tradingbot.strategy import SMACrossStrategy
from tradingbot.order import OrderManager
from tradingbot.state import BotState
from tradingbot.recovery import save_state, load_state
from tradingbot.commands.terminal import TerminalCommand
from tradingbot.commands.filewatcher import FileWatcher
from tradingbot.utils.logging import setup_logger

logger = setup_logger()


def handle_command(text: str, state: BotState, orders: OrderManager):
    """Handle commands from terminal."""
    parts = text.strip().split()
    if not parts:
        return
    cmd = parts[0]
    if cmd == "/status":
        logger.info("State: %s", state.symbols)
    elif cmd == "/buy" and len(parts) >= 3:
        symbol = parts[1].upper()
        qty = int(parts[2])
        orders.submit(symbol, "BUY", qty)
    elif cmd == "/pause" and len(parts) >= 2:
        symbol = parts[1].upper()
        state.ensure_symbol(symbol).paused = True
        logger.info("Paused %s", symbol)


def handle_json_command(cmd: Dict, state: BotState, orders: OrderManager):
    """Handle commands from command file."""
    action = cmd.get("action")
    symbol = cmd.get("symbol")
    qty = cmd.get("qty", 1)
    if action == "buy":
        orders.submit(symbol, "BUY", qty)
    elif action == "pause":
        state.ensure_symbol(symbol).paused = True
        logger.info("Paused %s", symbol)


def main():
    market = MarketData(SYMBOLS)
    strategy = SMACrossStrategy()
    orders = OrderManager()
    state = load_state(SYMBOLS)

    terminal = TerminalCommand(lambda txt: handle_command(txt, state, orders))
    terminal.start()
    watcher = FileWatcher("commands.json", lambda cmd: handle_json_command(cmd, state, orders))
    watcher.start()

    try:
        while True:
            market.update()
            for sym in SYMBOLS:
                price = market.get_price(sym)
                signal = strategy.on_price(sym, price)
                sym_state = state.ensure_symbol(sym)
                if sym_state.paused:
                    continue
                if signal == "BUY":
                    orders.submit(sym, "BUY", 1)
                elif signal == "SELL":
                    orders.submit(sym, "SELL", 1)
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Stopping bot...")
    finally:
        save_state(state)


if __name__ == "__main__":
    main()
