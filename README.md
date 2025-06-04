# TradingBot Project

This repository contains a modular trading bot for educational purposes. It demonstrates how to structure a Python project for algorithmic trading with simulated market data, a simple SMA crossover strategy and a command system.

## Structure

- `tradingbot/main.py` – entry point and trading loop
- `tradingbot/market.py` – price data provider (simulation)
- `tradingbot/strategy.py` – SMA cross strategy
- `tradingbot/order.py` – order management
- `tradingbot/state.py` – runtime state
- `tradingbot/recovery.py` – persistence of state
- `tradingbot/commands` – interfaces for controlling the bot (terminal, file watcher, telegram)
- `tradingbot/utils` – logging helper and simple timer
- `tradingbot/data/recovery.json` – state snapshot

The project also contains unit test placeholders under `tests/`.

## Quick start

```bash
pip install -r tradingbot/requirements.txt
python -m tradingbot.main
```

**Note:** always start the bot with the ``-m`` flag so that Python treats
``tradingbot`` as a package. Running ``python tradingbot/main.py`` would not
resolve imports correctly.
