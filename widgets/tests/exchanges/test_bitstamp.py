import pytest
from spacewink.exchanges import Bitstamp


@pytest.fixture
def exchange():
    return Bitstamp()


def test_get_markets(exchange):
    markets = exchange.get_markets()
    assert len(markets) > 0
    assert all(market['symbol'] for market in markets)


def test_get_market_ticker(exchange):
    market_ticker = exchange.get_market_ticker('btcusd')
    assert market_ticker is not None
    assert market_ticker['symbol'] == 'btcusd'


def test_get_market_depth(exchange):
    market_depth = exchange.get_market_depth('btcusd')
    assert market_depth is not None
    assert market_depth['bids'] is not None
    assert market_depth['asks'] is not None


def test_get_market_trades(exchange):
    market_trades = exchange.get_market_trades('btcusd')
    assert market_trades is not None
    assert all(trade['timestamp'] is not None for trade in market_trades)


def test_get_market_candles(exchange):
    market_candles = exchange.get_market_candles('btcusd', '1d')
    assert market_candles is not None
    assert all(candle['timestamp'] is not None for candle in market_candles)
