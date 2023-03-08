from abc import ABC, abstractmethod
import pandas as pd
from typing import List

class Strategy(ABC):
    """
    The base class for all strategies. 
    """

    @abstractmethod
    def set_config(self, config: dict) -> None:
        """
        Set the configuration parameters for the strategy.

        Parameters
        ----------
        config : dict
            A dictionary containing the configuration parameters for the strategy.
        """
        pass

    @abstractmethod
    def run(self) -> pd.DataFrame:
        """
        Run the strategy and return the DataFrame of signals.

        Returns
        -------
        pd.DataFrame
            A DataFrame of signals.
        """
        pass

    @abstractmethod
    def get_signal(self, asset: str, date: str) -> int:
        """
        Get the signal for the specified asset and date.

        Parameters
        ----------
        asset : str
            The asset symbol.
        date : str
            The date in the format YYYY-MM-DD.

        Returns
        -------
        int
            The signal for the specified asset and date. -1 for sell, 0 for hold, and 1 for buy.
        """
        pass

    @abstractmethod
    def get_all_signals(self, assets: List[str], dates: List[str]) -> pd.DataFrame:
        """
        Get the signals for the specified assets and dates.

        Parameters
        ----------
        assets : list of str
            The asset symbols.
        dates : list of str
            The dates in the format YYYY-MM-DD.

        Returns
        -------
        pd.DataFrame
            A DataFrame of signals.
        """
        pass
