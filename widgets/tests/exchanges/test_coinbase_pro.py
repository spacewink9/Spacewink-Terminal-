import pytest
import responses
import requests

from spacewink.exchanges.coinbase_pro import CoinbasePro
from spacewink.utils import Timeframe


@responses.activate
def test_get_historical_data():
    # mock response
    data = [
        [1621468800, 39060.2, 39287.56, 38879.25, 39273.48, 4075.57208926],
        [1621465200, 39109.92, 39395.0, 38960.87, 39060.19, 4479.45001899],
        [1621461600, 38785.69, 39197.24, 38785.69, 39109.92, 3294.0882874]
    ]
    responses.add(
        responses.GET,
        f'{CoinbasePro.REST_URL}/products/BTC-USD/candles',
        json=data,
        status=200
    )

    # initialize exchange class
    exchange = CoinbasePro()

    # test getting data for one day
    historical_data = exchange.get_historical_data('BTC-USD', Timeframe.ONE_DAY)
    assert len(historical_data) == 3
    assert historical_data[0].open == 39060.2
    assert historical_data[1].close == 39060.19
    assert historical_data[2].volume == 3294.0882874

    # test getting data for one hour
    historical_data = exchange.get_historical_data('BTC-USD', Timeframe.ONE_HOUR)
    assert len(historical_data) == 3
    assert historical_data[0].open == 39060.2
    assert historical_data[1].close == 39060.19
    assert historical_data[2].volume == 3294.0882874


@responses.activate
def test_get_current_price():
    # mock response
    data = {'price': '39010.35'}
    responses.add(
        responses.GET,
        f'{CoinbasePro.REST_URL}/products/BTC-USD/ticker',
        json=data,
        status=200
    )

    # initialize exchange class
    exchange = CoinbasePro()

    # test getting current price
    current_price = exchange.get_current_price('BTC-USD')
    assert current_price == 39010.35


def test_get_candles():
    # initialize exchange class
    exchange = CoinbasePro()

    # test getting candles
    candles = exchange.get_candles('BTC-USD', '2022-03-01', '2022-03-02')
    assert len(candles) == 1
    assert candles[0].open == 39060.2
    assert candles[0].close == 39273.48
    assert candles[0].low == 38879.25
    assert candles[0].high == 39287.56
    assert candles[0].volume == 4075.57208926


def test_get_account_balance():
    # initialize exchange class
    exchange = CoinbasePro()

    # test getting account balance
    with pytest.raises(requests.exceptions.HTTPError):
        exchange.get_account_balance('fake_api_key', 'fake_secret_key', 'fake_passphrase')
