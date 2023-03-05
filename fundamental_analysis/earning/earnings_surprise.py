import pandas as pd
import yfinance as yf

def get_earnings_surprise(ticker, start_date, end_date):
    # Fetch the earnings data for the specified period
    earnings = yf.download(ticker, start=start_date, end=end_date, interval='1d', group_by='ticker', auto_adjust=True, prepost=True)
    earnings = earnings[earnings['Earnings'].notnull()]
    
    # Calculate the earnings surprise for each earnings release
    earnings['Actual_EPS'] = earnings['Earnings']['EPS']
    earnings['Expected_EPS'] = earnings['Earnings']['EPSSurprise']
    earnings['Earnings_Surprise'] = earnings['Actual_EPS'] - earnings['Expected_EPS']
    
    return earnings[['Actual_EPS', 'Expected_EPS', 'Earnings_Surprise']]
