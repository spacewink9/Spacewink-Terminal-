from typing import List, Tuple
import pandas as pd


class BacktestTrade:
    """
    A class to represent a single trade in a backtest.

    Attributes
    ----------
    symbol : str
        The symbol of the traded asset.
    entry_time : pd.Timestamp
        The timestamp when the trade was entered.
    exit_time : pd.Timestamp or None
        The timestamp when the trade was exited, or None if the trade is still open.
    entry_price : float
        The price at which the trade was entered.
    exit_price : float or None
        The price at which the trade was exited, or None if the trade is still open.
    quantity : float
        The quantity of the traded asset.
    direction : str
        The direction of the trade, either 'long' or 'short'.
    exit_reason : str or None
        The reason why the trade was exited, or None if the trade is still open.
    """

    def __init__(
        self,
        symbol: str,
        entry_time: pd.Timestamp,
        entry_price: float,
        quantity: float,
        direction: str,
    ):
        """
        Parameters
        ----------
        symbol : str
            The symbol of the traded asset.
        entry_time : pd.Timestamp
            The timestamp when the trade was entered.
        entry_price : float
            The price at which the trade was entered.
        quantity : float
            The quantity of the traded asset.
        direction : str
            The direction of the trade, either 'long' or 'short'.
        """
        self.symbol = symbol
        self.entry_time = entry_time
        self.entry_price = entry_price
        self.quantity = quantity
        self.direction = direction

        self.exit_time = None
        self.exit_price = None
        self.exit_reason = None

    def exit_trade(self, exit_time: pd.Timestamp, exit_price: float, exit_reason: str):
        """
        Exit the trade.

        Parameters
        ----------
        exit_time : pd.Timestamp
            The timestamp when the trade was exited.
        exit_price : float
            The price at which the trade was exited.
        exit_reason : str
            The reason why the trade was exited.
        """
        self.exit_time = exit_time
        self.exit_price = exit_price
        self.exit_reason = exit_reason

    def get_profit(self) -> float:
        """
        Calculate the profit or loss of the trade.

        Returns
        -------
        float
            The profit or loss of the trade.
        """
        if self.exit_price is None:
            raise ValueError("Trade is still open")
        if self.direction == "long":
            return (self.exit_price - self.entry_price) * self.quantity
        elif self.direction == "short":
            return (self.entry_price - self.exit_price) * self.quantity
        else:
            raise ValueError(f"Invalid direction: {self.direction}")

    def get_holding_period(self) -> pd.Timedelta:
        """
        Calculate the holding period of the trade.

        Returns
        -------
        pd.Timedelta
            The holding period of the trade.
        """
        if self.exit_time is None:
            raise ValueError("Trade is still open")
        return self.exit_time - self.entry_time


class BacktestResult:
    """
    A class to represent the results of a backtest.

    Attributes
    ----------
    trades : List[BacktestTrade]
        A list of all the trades made during the backtest.
    initial_capital : float
        The initial capital of the backtest.
    final_capital : float
        The final capital of the backtest.
    total_return : float
        The total return of the trading period.
        
    Returns:
    -------
    float
        The total return on investment (ROI) over the trading period.
    """
    self.total_return = (final_capital - initial_capital) / initial_capital
    return self.total_return

def record_trade(self, trade: Trade):
    """
    Records a completed trade to the backtest.

    Parameters:
    ----------
    trade : Trade
        The completed trade to record.
    """
    self.trades.append(trade)

def get_trades(self) -> List[Trade]:
    """
    Returns a list of all completed trades in the backtest.

    Returns:
    -------
    List[Trade]
        A list of all completed trades in the backtest.
    """
    return self.trades

def get_num_trades(self) -> int:
    """
    Returns the total number of completed trades in the backtest.

    Returns:
    -------
    int
        The total number of completed trades in the backtest.
    """
    return len(self.trades)

def get_trade_summary(self) -> Dict[str, Any]:
    """
    Returns a summary of the trades in the backtest.

    Returns:
    -------
    Dict[str, Any]
        A dictionary containing information on the number of trades, the average
        return per trade, and the total return on investment (ROI).
    """
    num_trades = self.get_num_trades()
    if num_trades == 0:
        return {'num_trades': 0, 'avg_return': 0, 'total_return': 0}

    total_return = self.get_total_return()
    avg_return = total_return / num_trades
    return {'num_trades': num_trades, 'avg_return': avg_return, 'total_return': total_return}

def get_trade_history(self) -> pd.DataFrame:
    """
    Returns a DataFrame containing the trade history for the backtest.

    Returns:
    -------
    pd.DataFrame
        A DataFrame containing the trade history for the backtest.
    """
    return pd.DataFrame([trade.to_dict() for trade in self.trades])

