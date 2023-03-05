import yfinance as yf

def calculate_fair_value(ticker):
    """
    Calculate fair value of a stock based on discounted cash flow analysis.
    """
    # Get data
    stock = yf.Ticker(ticker)
    cash_flow = stock.cashflow
    free_cash_flow = cash_flow['Free Cash Flow']
    
    # Discount rate
    discount_rate = 0.1
    
    # Calculate present value of free cash flow
    present_value = []
    for i, value in enumerate(free_cash_flow):
        if i == 0:
            present_value.append(value)
        else:
            present_value.append(value / (1 + discount_rate)**i)
    present_value_sum = sum(present_value)
    
    # Terminal value
    last_fcf = free_cash_flow[-1]
    terminal_growth_rate = 0.03
    terminal_value = (last_fcf * (1 + terminal_growth_rate)) / (discount_rate - terminal_growth_rate)
    
    # Calculate fair value
    fair_value = present_value_sum + terminal_value
    
    return fair_value

def calculate_pe_ratio(ticker):
    """
    Calculate price-to-earnings ratio of a stock.
    """
    stock = yf.Ticker(ticker)
    earnings = stock.earnings
    pe_ratio = stock.info['regularMarketPrice'] / earnings['Earnings'].iloc[-1]
    
    return pe_ratio

def valuation_analysis(ticker):
    """
    Display valuation analysis of a stock.
    """
    # Calculate fair value and P/E ratio
    fair_value = calculate_fair_value(ticker)
    pe_ratio = calculate_pe_ratio(ticker)
    
    # Print results
    print(f"Valuation analysis for {ticker}:")
    print(f"Fair value: {fair_value:.2f}")
    print(f"P/E ratio: {pe_ratio:.2f}")
