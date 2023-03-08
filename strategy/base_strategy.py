from abc import ABC, abstractmethod
from typing import Dict, Any

import pandas as pd


class BaseStrategy(ABC):
    """
    The BaseStrategy class is an abstract base class that provides a template for creating trading strategies.
    """
    
    @abstractmethod
    def __init__(self, config: Dict[str, Any]):
        """
        Initializes the strategy with the provided configuration parameters.
        """
        self.config = config
        
    @abstractmethod
    def calculate_signals(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Calculates buy/sell signals based on the given dataframe.
        """
        pass
    
    def backtest(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Runs a backtest on the given dataframe and returns a new dataframe with the results.
        """
        signals = self.calculate_signals(dataframe)
        starting_capital = self.config['starting_capital']
        current_capital = starting_capital
        shares = 0
        trades = []
        for index, row in signals.iterrows():
            if row['signal'] == 'BUY':
                # Buy shares
                shares_to_buy = current_capital // row['close']
                shares += shares_to_buy
                current_capital -= shares_to_buy * row['close']
                trades.append(('BUY', row['date'], shares_to_buy, row['close']))
            elif row['signal'] == 'SELL':
                # Sell shares
                current_capital += shares * row['close']
                trades.append(('SELL', row['date'], shares, row['close']))
                shares = 0
                
        if shares > 0:
            # Sell remaining shares at the last closing price
            last_close = signals.iloc[-1]['close']
            current_capital += shares * last_close
            trades.append(('SELL', signals.iloc[-1]['date'], shares, last_close))
            
        # Calculate portfolio value over time
        portfolio_values = [starting_capital]
        shares_held = 0
        for trade in trades:
            if trade[0] == 'BUY':
                shares_held += trade[2]
                portfolio_values.append(starting_capital - (shares_held * trade[3]))
            elif trade[0] == 'SELL':
                shares_held -= trade[2]
                portfolio_values.append(starting_capital + (shares_held * trade[3]))
        
        # Create results dataframe
        results = pd.DataFrame({
            'date': signals['date'],
            'close': signals['close'],
            'signal': signals['signal'],
            'shares': [trade[2] for trade in trades],
            'price': [trade[3] for trade in trades],
            'portfolio_value': portfolio_values,
        })
        results.set_index('date', inplace=True)
        return results
    
    def get_config(self) -> Dict[str, Any]:
        """
        Returns the configuration parameters used by the strategy.
        """
        return self.config
    
    def set_config(self, config: Dict[str, Any]) -> None:
        """
        Updates the configuration parameters used by the strategy.
        """
            self.config = config
    self.tickers = self.config['tickers']
    self.interval = self.config['interval']
    self.start = self.config['start']
    self.end = self.config['end']

def set_data(self, data: Dict[str, pd.DataFrame]):
    self.data = data

def set_indicators(self, indicators: Dict[str, pd.DataFrame]):
    self.indicators = indicators

def buy_signal(self, ticker: str) -> bool:
    """
    Placeholder method for buy signal logic. Should be overridden by subclasses.
    """
    raise NotImplementedError

def sell_signal(self, ticker: str) -> bool:
    """
    Placeholder method for sell signal logic. Should be overridden by subclasses.
    """
    raise NotImplementedError

def generate_signals(self) -> Dict[str, pd.DataFrame]:
    """
    Generates buy and sell signals for each ticker based on the subclass' implementation of the buy_signal
    and sell_signal methods. Returns a dictionary of DataFrames where the keys are the ticker symbols and the values
    are the signals (1 = buy, -1 = sell, 0 = hold).
    """
    signals = {}
    for ticker in self.tickers:
        signals[ticker] = pd.DataFrame(index=self.data[ticker].index, columns=['signal'])
        signals[ticker].fillna(0, inplace=True)
        signals[ticker]['signal'] = np.where(self.buy_signal(ticker), 1, np.where(self.sell_signal(ticker), -1, 0))
    return signals

def backtest(self, signals: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    """
    Backtests the trading strategy based on the signals generated. Returns a DataFrame containing the backtest
    results.
    """
    portfolio = pd.DataFrame(index=self.data[self.tickers[0]].index, columns=['total'])
    portfolio['total'] = self.config['initial_capital']
    positions = {}
    for ticker in self.tickers:
        positions[ticker] = pd.DataFrame(index=self.data[ticker].index, columns=['position'])
        positions[ticker]['position'] = 0
    for i, (index, row) in enumerate(signals[self.tickers[0]].iterrows()):
        for ticker in self.tickers:
            if signals[ticker].iloc[i]['signal'] == 1:
                # Buy signal
                num_shares = portfolio.iloc[i]['total'] / self.data[ticker].iloc[i]['close']
                positions[ticker].iloc[i]['position'] = num_shares
                portfolio.iloc[i+1:]['total'] += (self.data[ticker].iloc[i+1:]['close'] - self.data[ticker].iloc[i]['close']) * num_shares
            elif signals[ticker].iloc[i]['signal'] == -1:
                # Sell signal
                num_shares = positions[ticker].iloc[i-1]['position']
                positions[ticker].iloc[i]['position'] = 0
                portfolio.iloc[i+1:]['total'] += (self.data[ticker].iloc[i+1:]['close'] - self.data[ticker].iloc[i]['close']) * num_shares
    portfolio['returns'] = portfolio['total'].pct_change()
    portfolio['cumulative_returns'] = (1 + portfolio['returns']).cumprod() - 1
    portfolio['benchmark_returns'] = self.data[self.tickers[0]]['close'].pct_change()
    portfolio['cumulative_benchmark_returns'] = (1 + portfolio['benchmark_returns']).cumprod() - 1
    return portfolio

def run(self) -> pd.DataFrame:
    """
    Runs the backtest and returns a DataFrame containing the
    # Load data
    self.load_data()

    # Apply strategy
    self.apply_strategy()

    # Generate signals
    self.generate_signals()

    # Calculate position sizes
    self.calculate_position_sizes()

    # Place orders
    self.place_orders()

    # Return results
    return self.results

