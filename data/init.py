import pandas as pd
from pathlib import Path
from typing import List


class DataHandler:
    """
    A class for loading and processing financial data.
    """

    def __init__(self, data_dir: str):
        """
        Initializes the DataHandler.

        Parameters
        ----------
        data_dir : str
            The directory containing the financial data.
        """
        self.data_dir = Path(data_dir)

    def load_data(self, tickers: List[str], start_date: str, end_date: str, frequency: str = '1d') -> pd.DataFrame:
        """
        Loads financial data for specified tickers and date range.

        Parameters
        ----------
        tickers : List[str]
            The list of tickers to load data for.
        start_date : str
            The start date of the date range in yyyy-mm-dd format.
        end_date : str
            The end date of the date range in yyyy-mm-dd format.
        frequency : str, optional
            The frequency of the data, by default '1d'.

        Returns
        -------
        pd.DataFrame
            The financial data for the specified tickers and date range.
        """
        data = pd.DataFrame()

        for ticker in tickers:
            file_path = self.data_dir / f"{ticker}.csv"

            if file_path.is_file():
                ticker_data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
                ticker_data = ticker_data.loc[start_date:end_date]

                if frequency == '1d':
                    data[ticker] = ticker_data['Adj Close']
                elif frequency == '1m':
                    data[ticker] = ticker_data['Adj Close'].resample('M').last().ffill()
                elif frequency == '1y':
                    data[ticker] = ticker_data['Adj Close'].resample('Y').last().ffill()

        data.dropna(inplace=True)

        return data

    def load_macro_data(self, data_name: str) -> pd.DataFrame:
        """
        Loads macro-economic data.

        Parameters
        ----------
        data_name : str
            The name of the macro-economic data to load.

        Returns
        -------
        pd.DataFrame
            The macro-economic data.
        """
        file_path = self.data_dir / f"{data_name}.csv"
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)

        return data

    def load_futures_data(self, contract_name: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Loads futures data.

        Parameters
        ----------
        contract_name : str
            The name of the futures contract to load.
        start_date : str
            The start date of the date range in yyyy-mm-dd format.
        end_date : str
            The end date of the date range in yyyy-mm-dd format.

        Returns
        -------
        pd.DataFrame
            The futures data.
        """
        file_path = self.data_dir / f"{contract_name}.csv"
        data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
        data = data.loc[start_date:end_date]

        return data
