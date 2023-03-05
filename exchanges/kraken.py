import krakenex
from .base_exchange import BaseExchange


class Kraken(BaseExchange):
    def __init__(self, api_key=None, api_secret=None):
        super().__init__(api_key, api_secret)
        self.client = krakenex.API()

    def get_ticker(self, symbol):
        data = self.client.query_public('Ticker', {'pair': symbol})['result']
        return {
            'bid': float(data[symbol]['b'][0]),
            'ask': float(data[symbol]['a'][0]),
            'last_price': float(data[symbol]['c'][0])
        }

    def get_order_book(self, symbol, depth=20):
        data = self.client.query_public('Depth', {'pair': symbol, 'count': depth})['result'][symbol]
        bids = [{'price': float(price), 'size': float(size)} for price, size in data['bids']]
        asks = [{'price': float(price), 'size': float(size)} for price, size in data['asks']]
        return {'bids': bids, 'asks': asks}

    def place_limit_order(self, symbol, side, quantity, price):
        params = {
            'pair': symbol,
            'type': 'buy' if side == 'buy' else 'sell',
            'ordertype': 'limit',
            'price': price,
            'volume': quantity
        }
        data = self.client.query_private('AddOrder', params)
        if data['error']:
            raise Exception(data['error'])
        return data['result']['txid'][0]

    def cancel_order(self, order_id):
        data = self.client.query_private('CancelOrder', {'txid': order_id})
        if data['error']:
            raise Exception(data['error'])
        return True

    def get_order_status(self, order_id):
        data = self.client.query_private('QueryOrders', {'txid': order_id})['result']
        if not data:
            return None
        status = data[order_id]['status']
        if status == 'open':
            return 'active'
        elif status == 'closed':
            return 'filled'
        elif status == 'canceled':
            return 'cancelled'
        else:
            return 'unknown'

    def get_open_orders(self):
        data = self.client.query_private('OpenOrders')['result']['open']
        return [{'id': order_id, 'symbol': order['descr']['pair'], 'side': order['descr']['type'],
                 'quantity': float(order['vol']), 'price': float(order['descr']['price']),
                 'timestamp': order['opentm']} for order_id, order in data.items()]

    def get_account_balance(self):
        data = self.client.query_private('Balance')['result']
        return {currency: float(balance) for currency, balance in data.items()}

    def get_trade_history(self, symbol=None, start_time=None, end_time=None):
        params = {}
        if symbol:
            params['pair'] = symbol
        if start_time:
            params['start'] = start_time
        if end_time:
            params['end'] = end_time
        data = self.client.query_private('TradesHistory', params)['result']['trades']
        return [{'id': trade_id, 'symbol': trade['pair'], 'side': trade['type'],
                 'quantity': float(trade['vol']), 'price': float(trade['price']),
                 'timestamp': trade['time']} for trade_id, trade in data.items()]
