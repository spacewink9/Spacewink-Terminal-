import pandas as pd
import numpy as np

class DataAnalytics:
    def __init__(self, data):
        self.data = data
        
    def compute_returns(self, freq='daily'):
        """Compute the returns of the assets in the data.

        Parameters
        ----------
        freq : str, optional
            The frequency of the returns computation. 
            Default is 'daily'.

        Returns
        -------
        pd.DataFrame
            The returns of the assets.
        """
        if freq == 'daily':
            returns = self.data.pct_change()
        elif freq == 'monthly':
            returns = self.data.resample('M').ffill().pct_change()
        elif freq == 'annual':
            returns = self.data.resample('Y').ffill().pct_change()
        else:
            raise ValueError('Invalid frequency.')
            
        return returns
    
    def compute_statistics(self, freq='daily'):
        """Compute the statistics of the assets.

        Parameters
        ----------
        freq : str, optional
            The frequency of the statistics computation. 
            Default is 'daily'.

        Returns
        -------
        pd.DataFrame
            The statistics of the assets.
        """
        returns = self.compute_returns(freq)
        
        statistics = pd.DataFrame(index=['mean', 'std', 'skewness', 'kurtosis', 'sharpe'], 
                                  columns=self.data.columns)
        
        statistics.loc['mean'] = returns.mean()
        statistics.loc['std'] = returns.std()
        statistics.loc['skewness'] = returns.skew()
        statistics.loc['kurtosis'] = returns.kurtosis()
        statistics.loc['sharpe'] = returns.mean() / returns.std() * np.sqrt(252)
        
        return statistics
    
    def compute_drawdowns(self):
        """Compute the drawdowns of the assets.

        Returns
        -------
        pd.DataFrame
            The drawdowns of the assets.
        """
        peak = self.data.cummax()
        drawdowns = (self.data - peak) / peak
        
        return drawdowns
