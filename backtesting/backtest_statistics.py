import numpy as np
import pandas as pd


def calculate_returns(prices: pd.Series) -> pd.Series:
    """
    Calculates the returns of a price series.

    Parameters
    ----------
    prices : pd.Series
        A series of prices.

    Returns
    -------
    pd.Series
        A series of returns.
    """
    return prices.pct_change(1)


def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    """
    Calculates the cumulative returns of a return series.

    Parameters
    ----------
    returns : pd.Series
        A series of returns.

    Returns
    -------
    pd.Series
        A series of cumulative returns.
    """
    return (1 + returns).cumprod() - 1


def calculate_annualized_returns(returns: pd.Series, trading_days: int = 252) -> float:
    """
    Calculates the annualized return of a return series.

    Parameters
    ----------
    returns : pd.Series
        A series of returns.
    trading_days : int, optional
        The number of trading days in a year, by default 252.

    Returns
    -------
    float
        The annualized return.
    """
    return np.power(1 + returns.mean(), trading_days) - 1


def calculate_annualized_volatility(returns: pd.Series, trading_days: int = 252) -> float:
    """
    Calculates the annualized volatility of a return series.

    Parameters
    ----------
    returns : pd.Series
        A series of returns.
    trading_days : int, optional
        The number of trading days in a year, by default 252.

    Returns
    -------
    float
        The annualized volatility.
    """
    return returns.std() * np.sqrt(trading_days)


def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate: float = 0, trading_days: int = 252) -> float:
    """
    Calculates the Sharpe ratio of a return series.

    Parameters
    ----------
    returns : pd.Series
        A series of returns.
    risk_free_rate : float, optional
        The risk-free rate, by default 0.
    trading_days : int, optional
        The number of trading days in a year, by default 252.

    Returns
    -------
    float
        The Sharpe ratio.
    """
    excess_returns = returns - risk_free_rate
    annualized_excess_returns = calculate_annualized_returns(excess_returns, trading_days)
    annualized_volatility = calculate_annualized_volatility(returns, trading_days)
    return annualized_excess_returns / annualized_volatility


def calculate_max_drawdown(returns: pd.Series) -> float:
    """
    Calculates the maximum drawdown of a return series.

    Parameters
    ----------
    returns : pd.Series
        A series of returns.

    Returns
    -------
    float
        The maximum drawdown.
    """
    cumulative_returns = calculate_cumulative_returns(returns)
    max_drawdown = (cumulative_returns - cumulative_returns.cummax()).min()
    return max_drawdown


def calculate_cagr(initial_capital: float, final_capital: float, num_years: float) -> float:
    """
    Calculates the Compound Annual Growth Rate (CAGR) given the initial and final capital and number of years.

    Parameters
    ----------
    initial_capital : float
        The initial capital.
    final_capital : float
        The final capital.
    num_years : float
        The number of years.

    Returns
    -------
    float
        The CAGR.
   
    def cagr(self) -> float:
        """Calculate the compound annual growth rate (CAGR) of the backtest."""
        years = (self.end_date - self.start_date).days / 365.25
        return (self.final_capital / self.initial_capital) ** (1 / years) - 1

    def sharpe_ratio(self, risk_free_rate: float = 0.0) -> float:
        """Calculate the Sharpe ratio of the backtest."""
        returns = self.returns()
        excess_returns = returns - risk_free_rate
        std_dev = excess_returns.std()
        return (returns.mean() - risk_free_rate) / std_dev if std_dev != 0 else 0.0

    def sortino_ratio(self, target_return: float = 0.0) -> float:
        """Calculate the Sortino ratio of the backtest."""
        returns = self.returns()
        downside_returns = returns[returns < target_return]
        std_dev = downside_returns.std()
        return (returns.mean() - target_return) / std_dev if std_dev != 0 else 0.0

    def max_drawdown(self) -> float:
        """Calculate the maximum drawdown of the backtest."""
        peak = self.equity_curve.expanding().max()
        drawdown = (self.equity_curve - peak) / peak
        return drawdown.min()

    def calmar_ratio(self) -> float:
        """Calculate the Calmar ratio of the backtest."""
        cagr = self.cagr()
        max_drawdown = self.max_drawdown()
        return cagr / abs(max_drawdown) if max_drawdown != 0 else 0.0
