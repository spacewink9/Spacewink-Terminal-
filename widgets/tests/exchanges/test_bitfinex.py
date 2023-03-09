import unittest
from exchanges.bitfinex import BitfinexClient

class TestBitfinexClient(unittest.TestCase):
    def setUp(self):
        self.client = BitfinexClient()

    def test_get_ticker(self):
        ticker = self.client.get_ticker('btcusd')
        self.assertIsNotNone(ticker)
        self.assertIsInstance(ticker, dict)
        self.assertIn('bid', ticker)
        self.assertIn('ask', ticker)
        self.assertIn('last_price', ticker)

    def test_get_orderbook(self):
        orderbook = self.client.get_orderbook('btcusd')
        self.assertIsNotNone(orderbook)
        self.assertIsInstance(orderbook, dict)
        self.assertIn('bids', orderbook)
        self.assertIn('asks', orderbook)

    def test_get_trades(self):
        trades = self.client.get_trades('btcusd')
        self.assertIsNotNone(trades)
        self.assertIsInstance(trades, list)
        self.assertGreater(len(trades), 0)
        self.assertIsInstance(trades[0], dict)
        self.assertIn('timestamp', trades[0])
        self.assertIn('amount', trades[0])
        self.assertIn('price', trades[0])
        self.assertIn('type', trades[0])
