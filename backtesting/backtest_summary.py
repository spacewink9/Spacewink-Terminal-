import pandas as pd
from typing import Dict, List


class BacktestSummary:
    """
    A class to summarize the results of a backtest.

    Attributes:
    - trades: A list of trades executed during the backtest.
    """

    def __init__(self, trades: List[Dict[str, any]]):
        """
        Initializes a new instance of the BacktestSummary class.

        Arguments:
        - trades: A list of trades executed during the backtest.
        """
        self.trades = trades

    def get_trade_log(self) -> pd.DataFrame:
        """
        Returns a DataFrame containing the details of the trades executed during the backtest.

        The DataFrame contains the following columns:
        - date: The date on which the trade was executed.
        - ticker: The ticker symbol of the security traded.
        - order_type: The type of the order (buy/sell).
        - quantity: The quantity of shares traded.
        - price: The price at which the shares were traded.
        - fees: The transaction fees associated with the trade.
        """
        trade_log = pd.DataFrame(self.trades)
        trade_log['fees'] = trade_log['fees'].fillna(0)
        trade_log['fees'] = trade_log['fees'].round(2)
        trade_log = trade_log[['date', 'ticker', 'order_type', 'quantity', 'price', 'fees']]
        return trade_log

    def get_trade_metrics(self) -> Dict[str, float]:
        """
        Returns a dictionary containing various metrics related to the trades executed during the backtest.

        The metrics returned by this function are:
        - num_trades: The total number of trades executed.
        - num_winners: The number of winning trades.
        - num_losers: The number of losing trades.
        - win_rate: The percentage of winning trades.
        - loss_rate: The percentage of losing trades.
        - average_return: The average return per trade (including fees).
        - average_win: The average return per winning trade (including fees).
        - average_loss: The average return per losing trade (including fees).
        - total_return: The total return (including fees) of the backtest.
        """
        trade_log = pd.DataFrame(self.trades)
        trade_log['fees'] = trade_log['fees'].fillna(0)
        trade_log['net_profit'] = trade_log['return'] - trade_log['fees']
        num_trades = len(trade_log)
        num_winners = len(trade_log[trade_log['net_profit'] > 0])
        num_losers = len(trade_log[trade_log['net_profit'] < 0])
        win_rate = num_winners / num_trades * 100
        loss_rate = num_losers / num_trades * 100
        average_return = trade_log['net_profit'].mean()
        average_win = trade_log[trade_log['net_profit'] > 0]['net_profit'].mean()
        average_loss = trade_log[trade_log['net_profit'] < 0]['net_profit'].mean()
        total_return = trade_log['net_profit'].sum()
        return {
            'num_trades': num_trades,
            'num_winners': num_winners,
            'num_losers': num_losers,
            'win_rate': win_rate,
            'loss_rate': loss_rate,
            'average_return': average_return,
            'average_win': average_win,
            'avg_trade_return': avg_trade_return,
'max_drawdown': max_drawdown,
'max_drawdown_pct': max_drawdown_pct,
'sharpe_ratio': sharpe_ratio,
'sortino_ratio': sortino_ratio,
'cagr': cagr,
'total_return': total_return,
'win_rate': win_rate,
'profit_factor': profit_factor
}

def plot_results(self):
"""
Plot the equity curve and drawdowns
"""
plt.plot(self.equity_curve)
plt.plot(self.drawdowns['drawdown'], linestyle='dotted')
plt.fill_between(self.drawdowns.index, self.drawdowns['drawdown'], alpha=0.2)
plt.title('Equity Curve')
plt.xlabel('Date')
plt.ylabel('Equity')
plt.show()

def export_results(self, filepath):
"""
Export the backtest results to a CSV file
"""
results = {
'num_trades': self.num_trades,
'avg_trade_return': self.avg_trade_return,
'max_drawdown': self.max_drawdown,
'max_drawdown_pct': self.max_drawdown_pct,
'sharpe_ratio': self.sharpe_ratio,
'sortino_ratio': self.sortino_ratio,
'cagr': self.cagr,
'total_return': self.total_return,
'win_rate': self.win_rate,
'profit_factor': self.profit_factor
}
pd.DataFrame.from_dict(results, orient='index').to_csv(filepath)

def print_summary(self):
"""
Print a summary of the backtest results to the console
"""
print('Backtest Summary')
print('----------------')
print(f'Ticker: {self.ticker}')
print(f'Start Date: {self.start_date}')
print(f'End Date: {self.end_date}')
print(f'Timeframe: {self.timeframe}')
print(f'Trading Strategy: {self.strategy.class.name}')
print(f'Total Trades: {self.num_trades}')
print(f'Win Rate: {self.win_rate:.2%}')
print(f'Profit Factor: {self.profit_factor:.2f}')
print(f'Average Trade Return: {self.avg_trade_return:.2%}')
print(f'Max Drawdown: {self.max_drawdown:.2f} ({self.max_drawdown_pct:.2%})')
print(f'Sharpe Ratio: {self.sharpe_ratio:.2f}')
print(f'Sortino Ratio: {self.sortino_ratio:.2f}')
print(f'Total Return: {self.total_return:.2%}')
print(f'CAGR: {self.cagr:.2%}')
print(f'Total Return: {self.total_return:.2%}')

        # Print individual trade metrics
        print('\nIndividual Trade Metrics:')
        print(f"{'Trade #':<10} {'Entry Date':<20} {'Exit Date':<20} {'Days Held':<10} {'Return':<20}")
        for i, trade in enumerate(self.trades):
            print(f"{i:<10} {trade.entry_date:<20} {trade.exit_date:<20} {trade.days_held:<10} {trade.return_pct:<20}")

        # Plot equity curve and drawdowns
        fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True, figsize=(12, 8))
        self.equity_curve.plot(ax=axes[0])
        axes[0].set_ylabel('Equity')
        axes[0].set_title('Equity Curve')
        self.drawdowns.plot(ax=axes[1])
        axes[1].set_ylabel('Drawdown')
        axes[1].set_title('Drawdowns')

        # Print and return summary metrics
        summary_metrics = {
            'total_return': self.total_return,
            'annualized_return': self.annualized_return,
            'max_drawdown': self.max_drawdown,
            'max_drawdown_pct': self.max_drawdown_pct,
            'sharpe_ratio': self.sharpe_ratio,
            'sortino_ratio': self.sortino_ratio,
            'num_trades': self.num_trades,
            'win_rate': self.win_rate,
            'profit_factor': self.profit_factor,
            'avg_return_pct': self.avg_return_pct,
            'max_return_pct': self.max_return_pct,
            'min_return_pct': self.min_return_pct,
            'avg_return': self.avg_return,
            'max_return': self.max_return,
            'min_return': self.min_return
        }
        print('\nSummary Metrics:')
        for metric, value in summary_metrics.items():
            print(f"{metric.capitalize().replace('_', ' '):<20}: {value:.2f}")
        return summary_metrics



