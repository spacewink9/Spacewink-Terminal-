import pandas as pd
from typing import List


class DataCleanUp:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir

    def clean_data(self, symbols: List[str], freq: str) -> None:
        """
        Cleans the data for the specified symbols and frequency.

        Parameters
        ----------
        symbols : List[str]
            List of symbols for which to clean data.
        freq : str
            The frequency of the data (e.g. '1D', '1H', '1T').

        Returns
        -------
        None
        """

        # Loop over each symbol
        for symbol in symbols:
            # Load the data
            data_path = f"{self.data_dir}/{symbol}_{freq}.csv"
            data = pd.read_csv(data_path, index_col=0, parse_dates=True)

            # Fill missing values
            data = data.fillna(method='ffill')

            # Remove duplicates
            data = data[~data.index.duplicated(keep='first')]

            # Save the cleaned data
            data.to_csv(data_path)
