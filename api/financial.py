import yfinance as yf

class FinancialAPI:
    def __init__(self):
        self.tickers = {}

    def get_data(self, symbol, start_date=None, end_date=None, interval='1d', source='yfinance'):
        """
        Get financial data for a given symbol and time range.

        Parameters
        ----------
        symbol : str
            The stock symbol to retrieve data for.
        start_date : str
            The start date of the data in the format "YYYY-MM-DD".
        end_date : str
            The end date of the data in the format "YYYY-MM-DD".
        interval : str
            The frequency of the data to retrieve. Can be '1d', '1wk', or '1mo'.
        source : str
            The source of the data. Can be 'yfinance' or 'other'.

        Returns
        -------
        pandas.DataFrame
            The financial data for the given symbol and time range.
        """
        if source == 'yfinance':
            if symbol not in self.tickers:
                self.tickers[symbol] = yf.Ticker(symbol)

            ticker = self.tickers[symbol]

            if start_date is None:
                history = ticker.history(period='max', interval=interval)
            else:
                history = ticker.history(start=start_date, end=end_date, interval=interval)

            return history

        else:
            # Add code to retrieve data from other data sources.
            pass

    def get_quote(self, symbol, source='yfinance'):
        """
        Get the latest stock price quote for a given symbol.

        Parameters
        ----------
        symbol : str
            The stock symbol to retrieve the quote for.
        source : str
            The source of the data. Can be 'yfinance' or 'other'.

        Returns
        -------
        float
            The latest stock price quote for the given symbol.
        """
        if source == 'yfinance':
            if symbol not in self.tickers:
                self.tickers[symbol] = yf.Ticker(symbol)

            ticker = self.tickers[symbol]
            return ticker.info['regularMarketPrice']

        else:
            # Add code to retrieve quote from other data sources.
            pass
