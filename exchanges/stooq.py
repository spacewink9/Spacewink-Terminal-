import requests
import pandas as pd

class Stooq:

    BASE_URL = "https://stooq.com/q/l/"

    @staticmethod
    def get_historical_data(symbol: str, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Get historical data for a symbol from Stooq.

        Args:
            symbol (str): The symbol of the stock or asset.
            start_date (str): The start date in the format YYYYMMDD.
            end_date (str): The end date in the format YYYYMMDD.

        Returns:
            pd.DataFrame: A pandas DataFrame with the historical data.
        """
        url = f"{Stooq.BASE_URL}/s/{symbol}.us/d/{start_date}/{end_date}.csv"
        response = requests.get(url)
        data = pd.read_csv(url)
        return data
