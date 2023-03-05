import pandas as pd

def dividend_yield(ticker):
    """
    Calculates the dividend yield of a stock using the most recent annual dividend and the current stock price.
    
    Parameters:
    ticker (str): Stock symbol
    
    Returns:
    float: Dividend yield
    """
    # Collect stock price and dividend data using API calls
    stock_price = # API call to get current stock price
    dividend_data = # API call to get dividend data
    
    # Convert dividend data to a pandas dataframe
    dividend_df = pd.DataFrame(dividend_data)
    
    # Filter for most recent annual dividend payment
    most_recent_dividend = dividend_df.loc[dividend_df['frequency'] == 'annual'].sort_values(by='paymentDate', ascending=False).iloc[0]['amount']
    
    # Calculate dividend yield
    dividend_yield = (most_recent_dividend / stock_price) * 100
    
    return dividend_yield
