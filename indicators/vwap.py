from typing import List
from market_data.bar import Bar
from indicators.sma import SMA


class VWAP:
    """
    Volume Weighted Average Price (VWAP) indicator.
    """

    def __init__(self, window: int) -> None:
        """
        Constructor for the VWAP indicator.

        Parameters:
        window (int): The number of bars to use in the calculation.
        """
        self.window = window
        self.sma = SMA(window)

    def calculate(self, bars: List[Bar]) -> float:
        """
        Calculates the VWAP for the given bars.

        Parameters:
        bars (List[Bar]): A list of bars.

        Returns:
        float: The VWAP value.
        """
        typical_prices = [(bar.high + bar.low + bar.close) / 3 for bar in bars]
        volumes = [bar.volume for bar in bars]

        # Calculate the typical price * volume values
        tpv_values = [tp * vol for tp, vol in zip(typical_prices, volumes)]

        # Calculate the cumulative sum of the typical price * volume values and volumes
        tpv_cumulative_sum = [sum(tpv_values[:i+1]) for i in range(len(tpv_values))]
        volume_cumulative_sum = [sum(volumes[:i+1]) for i in range(len(volumes))]

        # Calculate the VWAP using the SMA
        vwap = self.sma.calculate(tpv_cumulative_sum, volume_cumulative_sum)

        return vwap
