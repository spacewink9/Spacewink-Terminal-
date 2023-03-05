from exchanges.exchange import BaseExchange

class CoinbasePro(BaseExchange):
    def __init__(self, api_key=None, api_secret=None, passphrase=None):
        super().__init__('Coinbase Pro', api_key, api_secret, passphrase)
        # initialize API client

    def get_order_book(self, symbol, depth=20):
        # get order book for a given symbol
        pass

    def get_ticker(self, symbol):
        # get ticker data for a given symbol
        pass

    def get_recent_trades(self, symbol, limit=100):
        # get recent trades for a given symbol
        pass

    def get_historical_trades(self, symbol, start_time=None, end_time=None, limit=None):
        # get historical trades for a given symbol
        pass

    def get_candles(self, symbol, interval, start_time=None, end_time=None, limit=None):
        # get OHLCV candles for a given symbol
        pass

    def create_order(self, symbol, side, type, quantity, price=None, stop_price=None, time_in_force=None):
        # create a new order for a given symbol
        pass

    def cancel_order(self, order_id):
        # cancel an existing order
        pass

    def get_order(self, order_id):
        # get details of an existing order
        pass

    def get_orders(self, symbol=None, status=None, limit=100):
        # get list of all orders, filtered by symbol and status
        pass

    def get_positions(self):
        # get list of all positions
        pass

    def get_account(self):
        # get account information
        pass

    def get_exchange_info(self):
        # get exchange information
        pass
