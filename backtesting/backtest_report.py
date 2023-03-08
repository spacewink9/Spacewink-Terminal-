import pandas as pd
import matplotlib.pyplot as plt
from typing import List

class BacktestReport:
    def __init__(self, results: pd.DataFrame):
        self.results = results
        self.pnl = self.compute_pnl()
        self.stats = self.compute_stats()
    
    def compute_pnl(self) -> pd.DataFrame:
        # Compute P&L
        ...
        return pnl
    
    def compute_stats(self) -> pd.Series:
        # Compute trading statistics
        ...
        return stats
    
    def plot_results(self):
        # Plot P&L and other relevant charts
        ...
    
    def summary(self) -> str:
        # Generate a summary of the backtest results
        ...
    
    def to_csv(self, filename: str):
        # Save backtest results to CSV
        ...
    
    def to_excel(self, filename: str):
        # Save backtest results to Excel
        ...
    
    def to_html(self, filename: str):
        # Save backtest results to HTML
        ...

def run_backtest(strategy, data: pd.DataFrame, **kwargs) -> BacktestReport:
    # Run backtest with given strategy and data
    ...
    return BacktestReport(results)
