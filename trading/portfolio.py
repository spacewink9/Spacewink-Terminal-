from typing import List
import pandas as pd

class Portfolio:
    def __init__(self, cash: float, holdings: List[dict] = None):
        """
        Initialize the Portfolio instance.

        Parameters
        ----------
        cash : float
            The amount of cash available for trading.
        holdings : list of dicts, optional
            A list of dictionaries representing the holdings in the portfolio. Each
            dictionary should have keys 'symbol' (str), 'quantity' (float), and
            'purchase_price' (float).
        """
        self.cash = cash
        self.holdings = holdings or []

    def add_cash(self, amount: float) -> None:
        """
        Add cash to the portfolio.

        Parameters
        ----------
        amount : float
            The amount of cash to add.
        """
        self.cash += amount

    def remove_cash(self, amount: float) -> None:
        """
        Remove cash from the portfolio.

        Parameters
        ----------
        amount : float
            The amount of cash to remove.
        """
        if self.cash < amount:
            raise ValueError('Insufficient cash')
        self.cash -= amount

    def add_holding(self, symbol: str, quantity: float, purchase_price: float) -> None:
        """
        Add a holding to the portfolio.

        Parameters
        ----------
        symbol : str
            The symbol of the security.
        quantity : float
            The quantity of the security.
        purchase_price : float
            The purchase price of the security.
        """
        self.holdings.append({
            'symbol': symbol,
            'quantity': quantity,
            'purchase_price': purchase_price
        })

    def remove_holding(self, symbol: str, quantity: float) -> None:
        """
        Remove a holding from the portfolio.

        Parameters
        ----------
        symbol : str
            The symbol of the security.
        quantity : float
            The quantity of the security to remove.
        """
        holding = next((h for h in self.holdings if h['symbol'] == symbol), None)
        if not holding:
            raise ValueError('Holding not found')
        if holding['quantity'] < quantity:
            raise ValueError('Insufficient quantity')
        holding['quantity'] -= quantity
        if holding['quantity'] == 0:
            self.holdings.remove(holding)

    def get_holdings(self) -> pd.DataFrame:
        """
        Get a DataFrame of the holdings in the portfolio.

        Returns
        -------
        pd.DataFrame
            A DataFrame with columns 'symbol' (str), 'quantity' (float),
            'purchase_price' (float), 'current_price' (float), 'market_value' (float),
            'unrealized_pnl' (float), and 'pct_change' (float).
        """
        from ..data import get_latest_prices

        holdings_df = pd.DataFrame(self.holdings)
        symbols = holdings_df['symbol'].tolist()
        prices_df = get_latest_prices(symbols)
        holdings_df = holdings_df.merge(prices_df, on='symbol')
        holdings_df['market_value'] = holdings_df['quantity'] * holdings_df['current_price']
        holdings_df['unrealized_pnl'] = holdings_df['market_value'] - \
            (holdings_df['quantity'] * holdings_df['purchase_price'])
        holdings_df['pct_change'] = holdings_df['current_price'] / \
            holdings_df['purchase_price'] - 1
        return holdings_df

    def get_market_value(self) -> float:
        """
        Get the current market value of the
    Returns
    -------
    float
        The market value of the portfolio.
    """
    market_value = 0.0
    for symbol, position in self.positions.items():
        current_price = self._data_handler.get_last_close(symbol)
        market_value += current_price * position
    return market_value

def get_unrealized_pnl(self) -> float:
    """
    Calculates the current unrealized P&L of the portfolio.

    Returns
    -------
    float
        The unrealized P&L of the portfolio.
    """
    unrealized_pnl = 0.0
    for symbol, position in self.positions.items():
        current_price = self._data_handler.get_last_close(symbol)
        cost_basis = self.cost_basis.get(symbol, 0.0)
        unrealized_pnl += (current_price - cost_basis) * position
    return unrealized_pnl

def get_realized_pnl(self) -> float:
    """
    Calculates the realized P&L of the portfolio.

    Returns
    -------
    float
        The realized P&L of the portfolio.
    """
    realized_pnl = 0.0
    for trade in self.trade_log:
        symbol = trade.symbol
        if trade.side == 'BUY':
            cost_basis = trade.price * trade.quantity
            self.cost_basis[symbol] = (self.cost_basis.get(symbol, 0.0) + cost_basis) / (trade.quantity + self.positions.get(symbol, 0.0))
            self.positions[symbol] = self.positions.get(symbol, 0.0) + trade.quantity
        else:
            self.positions[symbol] = self.positions.get(symbol, 0.0) - trade.quantity
            proceeds = trade.price * trade.quantity
            realized_pnl += proceeds - (self.cost_basis.get(symbol, 0.0) * trade.quantity)
    return realized_pnl

def get_total_pnl(self) -> float:
    """
    Calculates the total P&L of the portfolio.

    Returns
    -------
    float
        The total P&L of the portfolio.
    """
    return self.get_unrealized_pnl() + self.get_realized_pnl()def get_total_pnl(self) -> float:
    """
    Get the total profit and loss (P&L) of the portfolio.

    Returns
    -------
    float
        The total P&L of the portfolio.
    """
    return self.get_market_value() - self.initial_cash

def get_returns(self) -> float:
    """
    Get the returns of the portfolio as a percentage.

    Returns
    -------
    float
        The returns of the portfolio as a percentage.
    """
    total_pnl = self.get_total_pnl()
    initial_value = self.initial_cash + abs(self.get_total_fees())
    return total_pnl / initial_value * 100

def get_annualized_returns(self, years: float) -> float:
    """
    Get the annualized returns of the portfolio.

    Parameters
    ----------
    years : float
        The number of years for which to compute the annualized returns.

    Returns
    -------
    float
        The annualized returns of the portfolio.
    """
    returns = self.get_returns() / 100
    annualized_returns = (1 + returns) ** (1 / years) - 1
    return annualized_returns * 100

def get_sharpe_ratio(self, risk_free_rate: float) -> float:
    """
    Get the Sharpe ratio of the portfolio.

    Parameters
    ----------
    risk_free_rate : float
        The annualized risk-free rate.

    Returns
    -------
    float
        The Sharpe ratio of the portfolio.
    """
    daily_returns = self.get_daily_returns()
    excess_returns = daily_returns - risk_free_rate / 252
    sharpe_ratio = excess_returns.mean() / excess_returns.std(ddof=1) * np.sqrt(252)
    return sharpe_ratio

def get_max_drawdown(self) -> float:
    """
    Get the maximum drawdown of the portfolio.

    Returns
    -------
    float
        The maximum drawdown of the portfolio.
    """
    returns = self.get_returns() / 100
    cumulative_returns = (1 + returns).cumprod()
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    max_drawdown = drawdown.min() * 100
    return max_drawdown

def get_daily_returns(self) -> pd.Series:
    """
    Get the daily returns of the portfolio.

    Returns
    -------
    pd.Series
        The daily returns of the portfolio.
    """
    daily_values = self.portfolio_value.resample('D').last()
    daily_returns = daily_values.pct_change()
    daily_returns.iloc[0] = 0
    return daily_returns

def plot_performance(self):
    """
    Plot the performance of the portfolio.
    """
    plt.rcParams["figure.figsize"] = (10, 6)
    fig, ax = plt.subplots()

    ax.plot(self.portfolio_value.index, self.portfolio_value.values)
    ax.set_xlabel('Date')
    ax.set_ylabel('Portfolio Value ($)')
    ax.set_title('Portfolio Performance')

    plt.show()

  
