import yfinance as yf

def get_earnings_history(ticker):
    # Get the ticker data
    ticker_data = yf.Ticker(ticker)

    # Get the earnings history
    earnings_history = ticker_data.earnings

    # Return the earnings history
    return earnings_history
