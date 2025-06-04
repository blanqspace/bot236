import unittest
from tradingbot.strategy import SMACrossStrategy


class TestSMACrossStrategy(unittest.TestCase):
    def test_buy_signal(self):
        strategy = SMACrossStrategy(short_window=3, long_window=5)
        prices = [1, 2, 3, 4, 5, 6]
        signal = "HOLD"
        for p in prices:
            signal = strategy.on_price("TEST", p)
        self.assertEqual(signal, "BUY")


if __name__ == "__main__":
    unittest.main()
