import unittest
from unittest import mock
from datetime import datetime
from spacewink.exchanges.exchange import Exchange, Candlestick


class TestExchange(unittest.TestCase):

    def setUp(self):
        self.exchange = Exchange("TestExchange")

    def test_name(self):
        self.assertEqual(self.exchange.name, "TestExchange")

    def test_get_candlesticks(self):
        # Mocking the `get_candlesticks` method
        self.exchange.get_candlesticks = mock.Mock(return_value=[
            Candlestick(open_price=10, high_price=15, low_price=8, close_price=12, timestamp=datetime.now()),
            Candlestick(open_price=12, high_price=18, low_price=9, close_price=16, timestamp=datetime.now()),
            Candlestick(open_price=16, high_price=20, low_price=11, close_price=19, timestamp=datetime.now())
        ])
        candlesticks = self.exchange.get_candlesticks("BTC/USD", "1h", limit=3)

        self.assertEqual(len(candlesticks), 3)
        self.assertEqual(candlesticks[0].open_price, 10)
        self.assertEqual(candlesticks[1].close_price, 16)
        self.assertEqual(candlesticks[2].high_price, 20)

    def test_get_orderbook(self):
        # Mocking the `get_orderbook` method
        self.exchange.get_orderbook = mock.Mock(return_value={
            "bids": [
                [100, 5],
                [99, 10],
                [98, 15]
            ],
            "asks": [
                [101, 5],
                [102, 10],
                [103, 15]
            ]
        })
        orderbook = self.exchange.get_orderbook("BTC/USD")

        self.assertEqual(len(orderbook["bids"]), 3)
        self.assertEqual(len(orderbook["asks"]), 3)
        self.assertEqual(orderbook["bids"][0][0], 100)
        self.assertEqual(orderbook["asks"][1][1], 10)

    def test_get_ticker(self):
        # Mocking the `get_ticker` method
        self.exchange.get_ticker = mock.Mock(return_value={
            "symbol": "BTC/USD",
            "last_price": 50000,
            "volume": 1000
        })
        ticker = self.exchange.get_ticker("BTC/USD")

        self.assertEqual(ticker["symbol"], "BTC/USD")
        self.assertEqual(ticker["last_price"], 50000)
        self.assertEqual(ticker["volume"], 1000)

