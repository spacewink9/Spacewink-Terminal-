import unittest
from unittest.mock import MagicMock

from spacewink.exchanges.alpha_vantage import AlphaVantage


class TestAlphaVantage(unittest.TestCase):
    def setUp(self):
        self.api_key = "123456789"
        self.alpha_vantage = AlphaVantage(self.api_key)
        self.ticker = "AAPL"

    def test_get_price(self):
        self.alpha_vantage._make_request = MagicMock(return_value={"Global Quote": {"05. price": "135.98"}})
        price = self.alpha_vantage.get_price(self.ticker)
        self.assertEqual(price, 135.98)

    def test_get_historical_prices(self):
        self.alpha_vantage._make_request = MagicMock(return_value={
            "Time Series (Daily)": {
                "2022-02-28": {"4. close": "135.98"},
                "2022-02-27": {"4. close": "134.98"}
            }
        })
        prices = self.alpha_vantage.get_historical_prices(self.ticker, "2022-02-27", "2022-02-28")
        self.assertEqual(prices, {"2022-02-27": 134.98, "2022-02-28": 135.98})
