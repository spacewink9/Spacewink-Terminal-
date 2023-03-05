def get_historical_data(symbol, start_date, end_date, interval='1d'):
    """
    Retrieves historical price data for a given symbol, time range, and interval.

    :param symbol: str
        The symbol to retrieve data for (e.g. 'AAPL', 'MSFT', etc.)
    :param start_date: str
        The start date for the historical data in the format 'YYYY-MM-DD'
    :param end_date: str
        The end date for the historical data in the format 'YYYY-MM-DD'
    :param interval: str, optional (default='1d')
        The interval to retrieve data at ('1d', '1wk', '1mo', etc.)

    :return: pandas.DataFrame
        The historical price data for the symbol within the given time range and interval.
    """
    # TODO: Implement function
