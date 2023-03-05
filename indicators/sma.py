from typing import List
from indicators import Indicator
from market_data import Bar


class SMA(Indicator):
    """
    Simple Moving Average (SMA) Indicator
    """
    
    def __init__(self, window: int):
        """
        :param window: The window size (number of bars) for the SMA calculation.
        """
        super().__init__()
        self.window = window
        self.values = []
        
    def calculate(self, bars: List[Bar]) -> float:
        """
        Calculates the SMA for the given window and returns the current value.
        :param bars: A list of bars.
        :return: The current value of the SMA.
        """
        self.values.append(sum([bar.close for bar in bars[-self.window:]])/self.window)
        return self.values[-1]
