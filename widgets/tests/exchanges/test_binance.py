import unittest
from spacewink.exchanges.binance import BinanceClient

class TestBinanceClient(unittest.TestCase):
    def setUp(self):
        self.client = BinanceClient()

    def test_get_latest_price(self):
        symbol = 'BTCUSDT'
        result = self.client.get_latest_price(symbol)
        self.assertIsInstance(result, float)

    def test_get_klines(self):
        symbol = 'BTCUSDT'
        interval = '1h'
        result = self.client.get_klines(symbol, interval)
        self.assertIsInstance(result, list)
        self.assertGreater(len(result), 0)

    def test_get_orderbook(self):
        symbol = 'BTCUSDT'
        limit = 5
        result = self.client.get_orderbook(symbol, limit)
        self.assertIsInstance(result, dict)
        self.assertIn('bids', result)
        self.assertIn('asks', result)

if __name__ == '__main__':
    unittest.main()
