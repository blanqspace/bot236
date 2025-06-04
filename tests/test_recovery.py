import os
import json
import unittest
from tradingbot.state import BotState
from tradingbot.recovery import save_state, load_state
from tradingbot.config import RECOVERY_FILE


class TestRecovery(unittest.TestCase):
    def test_save_load(self):
        state = BotState()
        state.ensure_symbol("AAPL").position = 10
        save_state(state)
        loaded = load_state(["AAPL"]) 
        self.assertEqual(loaded.symbols["AAPL"].position, 10)
        os.remove(RECOVERY_FILE)


if __name__ == "__main__":
    unittest.main()
