import yfinance as yf

def get_weekly_losers():
    """
    Retrieves the top 10 weekly stock losers from Yahoo Finance.

    Returns:
    A list of dictionaries containing information about the top 10 weekly stock losers.
    """
    losers = yf.Tickers("losers")
    losers_weekly = losers.todays_sparkline
    weekly_data = []

    for ticker in losers_weekly:
        ticker_data = {}
        ticker_name = ticker.info['shortName']
        ticker_symbol = ticker.info['symbol']
        ticker_last_price = ticker.info['regularMarketPrice']
        ticker_change = ticker.info['regularMarketChangePercent']
        ticker_data['name'] = ticker_name
        ticker_data['symbol'] = ticker_symbol
        ticker_data['last_price'] = ticker_last_price
        ticker_data['change'] = ticker_change
        weekly_data.append(ticker_data)

    return weekly_data[:10] # Returns the top 10 weekly stock losers
