import pandas as pd


class BacktestPerformance:
    """Calculates performance metrics for a backtest."""

    def __init__(self, returns: pd.Series, benchmark_returns: pd.Series = None):
        """
        Parameters
        ----------
        returns : pd.Series
            The returns of the backtest.
        benchmark_returns : pd.Series, optional
            The returns of the benchmark, by default None.
        """
        self.returns = returns
        self.benchmark_returns = benchmark_returns

    @property
    def annualized_return(self) -> float:
        """Calculates the annualized return of the backtest."""
        return (1 + self.returns).prod() ** (252 / len(self.returns)) - 1

    @property
    def annualized_volatility(self) -> float:
        """Calculates the annualized volatility of the backtest."""
        return self.returns.std() * (252 ** 0.5)

    @property
    def sharpe_ratio(self) -> float:
        """Calculates the Sharpe ratio of the backtest."""
        return self.annualized_return / self.annualized_volatility

    @property
    def max_drawdown(self) -> float:
        """Calculates the maximum drawdown of the backtest."""
        cumulative_returns = (1 + self.returns).cumprod()
        running_max = cumulative_returns.cummax()
        drawdown = (cumulative_returns - running_max) / running_max
        return drawdown.min()

    @property
    def calmar_ratio(self) -> float:
        """Calculates the Calmar ratio of the backtest."""
        return self.annualized_return / abs(self.max_drawdown)

    @property
    def information_ratio(self) -> float:
        """Calculates the information ratio of the backtest."""
        excess_returns = self.returns - self.benchmark_returns
        return excess_returns.mean() / excess_returns.std()

    @property
    def omega_ratio(self) -> float:
        """Calculates the Omega ratio of the backtest."""
        threshold_return = 0
        return sum(self.returns[self.returns < threshold_return]) / abs(sum(self.returns[self.returns >= threshold_return]))

    @property
    def sortino_ratio(self) -> float:
        """Calculates the Sortino ratio of the backtest."""
        downside_returns = self.returns[self.returns < 0]
        downside_volatility = downside_returns.std() * (252 ** 0.5)
        return self.annualized_return / downside_volatility

    @property
    def value_at_risk(self) -> float:
        """Calculates the value-at-risk of the backtest."""
        return self.returns.quantile(0.05)

    @property
    def expected_shortfall(self) -> float:
        """Calculates the expected shortfall of the backtest."""
        return self.returns[self.returns <= self.value_at_risk].mean()
