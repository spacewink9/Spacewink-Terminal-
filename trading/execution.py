import time
import random


class Execution:
    def __init__(self, broker, symbol):
        self.broker = broker
        self.symbol = symbol

    def execute_market_order(self, quantity, side, wait_time=3):
        print(f"Executing {side} market order for {quantity} shares of {self.symbol}...")
        time.sleep(wait_time)  # simulate execution time
        executed_price = self.broker.get_last_price(self.symbol)
        return executed_price, quantity

    def execute_limit_order(self, quantity, side, limit_price, wait_time=3):
        print(f"Submitting {side} limit order for {quantity} shares of {self.symbol} at {limit_price}...")
        time.sleep(wait_time)  # simulate order submission time
        executed_price = self.broker.get_last_price(self.symbol)  # get current market price
        if side == 'buy' and executed_price <= limit_price:
            print(f"Order filled at {executed_price}")
            return executed_price, quantity
        elif side == 'sell' and executed_price >= limit_price:
            print(f"Order filled at {executed_price}")
            return executed_price, quantity
        else:
            print(f"Limit price not met. Cancelling order...")
            return None, None

    def execute_stop_order(self, quantity, side, stop_price, wait_time=3):
        print(f"Submitting {side} stop order for {quantity} shares of {self.symbol} at {stop_price}...")
        time.sleep(wait_time)  # simulate order submission time
        executed_price = self.broker.get_last_price(self.symbol)  # get current market price
        if side == 'buy' and executed_price >= stop_price:
            print(f"Order filled at {executed_price}")
            return executed_price, quantity
        elif side == 'sell' and executed_price <= stop_price:
            print(f"Order filled at {executed_price}")
            return executed_price, quantity
        else:
            print(f"Stop price not met. Cancelling order...")
            return None, None

    def execute_algo_order(self, quantity, side, algo_type, params, wait_time=3):
        print(f"Submitting {side} {algo_type} order for {quantity} shares of {self.symbol} with parameters: {params}...")
        time.sleep(wait_time)  # simulate order submission time
        executed_price = self.broker.get_last_price(self.symbol)  # get current market price
        if algo_type == 'TWAP':
            avg_price = self.execute_twap_order(quantity, side, params)
            if avg_price is not None:
                print(f"{algo_type} order filled with average price {avg_price}")
                return avg_price, quantity
            else:
                print(f"{algo_type} order cancelled.")
                return None, None
        elif algo_type == 'VWAP':
            avg_price = self.execute_vwap_order(quantity, side, params)
            if avg_price is not None:
                print(f"{algo_type} order filled with average price {avg_price}")
                return avg_price, quantity
            else:
                print(f"{algo_type} order cancelled.")
                return None, None
        else:
            print(f"Invalid algo type. Cancelling order...")
            return None, None

    def execute_vwap_order(self, symbol: str, side: str, quantity: float, start_time: str, end_time: str,
                        interval: str = '1min') -> List[Dict[str, Union[str, float]]]:
    """
    Executes a VWAP order for a given symbol and quantity over a specified time period.

    Parameters
    ----------
    symbol : str
        The symbol to trade.
    side : str
        The side of the order, either 'buy' or 'sell'.
    quantity : float
        The quantity to trade.
    start_time : str
        The start time of the VWAP period, in ISO format (e.g. '2022-03-05T09:30:00-05:00').
    end_time : str
        The end time of the VWAP period, in ISO format (e.g. '2022-03-05T09:30:00-05:00').
    interval : str, optional
        The interval of the historical data to use in the VWAP calculation, by default '1min'.

    Returns
    -------
    List[Dict[str, Union[str, float]]]
        A list of trade objects, each containing the trade timestamp, price, and quantity.
    """
    # Get historical data for the specified symbol and time period
    historical_data = self.api.get_historical_data(symbol, start_time, end_time, interval=interval)

    # Calculate the VWAP for each time interval
    vwap_values = []
    for i in range(len(historical_data)):
        if i == 0:
            vwap_values.append(historical_data[i]['close'])
        else:
            volume = historical_data[i]['volume']
            typical_price = (historical_data[i]['high'] + historical_data[i]['low'] + historical_data[i]['close']) / 3
            cumulative_tp_vol = sum([historical_data[j]['volume'] * (
                    (historical_data[j]['high'] + historical_data[j]['low'] + historical_data[j]['close']) / 3)
                                     for j in range(i)])
            vwap = cumulative_tp_vol / sum([historical_data[j]['volume'] for j in range(i)])
            vwap_values.append(vwap)

    # Normalize the VWAP values to the trading period
    total_vwap = sum(vwap_values)
    normalized_vwap_values = [vwap / total_vwap for vwap in vwap_values]

    # Execute the VWAP order
    trades = []
    remaining_quantity = quantity
    for i in range(len(historical_data)):
        trade_quantity = normalized_vwap_values[i] * quantity
        if trade_quantity > remaining_quantity:
            trade_quantity = remaining_quantity
        trade_price = historical_data[i]['close']
        trade = {'timestamp': historical_data[i]['timestamp'], 'price': trade_price, 'quantity': trade_quantity}
        if side == 'buy':
            self.portfolio.buy(symbol, trade_price, trade_quantity)
        elif side == 'sell':
            self.portfolio.sell(symbol, trade_price, trade_quantity)
        trades.append(trade)
        remaining_quantity -= trade_quantity
        if remaining_quantity <= 0:
            break

    return trades


