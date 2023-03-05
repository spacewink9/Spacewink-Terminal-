from screens.base_screen import BaseScreen
from market_data.market_data import MarketData
from indicators.macd import MACD
from indicators.bbands import BBands

class TechnicalAnalysisScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Technical Analysis Screen ===")
        symbol = self.get_user_input("Enter symbol to analyze: ")

        # Get market data for symbol
        bars = self.market_data.get_latest_bars(symbol, 200)
        close_prices = [bar.close_price for bar in bars]

        # Calculate MACD
        macd = MACD(close_prices)
        macd_values = macd.calculate()

        # Calculate Bollinger Bands
        bbands = BBands(close_prices, 20, 2)
        upper_bband, mid_bband, lower_bband = bbands.calculate()

        # Display results
        print(f"\nLatest {len(bars)} bars for {symbol}:")
        for bar in bars:
            print(bar)

        print(f"\nMACD values for {symbol}:")
        for i in range(len(macd_values)):
            print(f"Bar {i+1}: {macd_values[i]}")

        print(f"\nBollinger Bands for {symbol}:")
        for i in range(len(upper_bband)):
            print(f"Bar {i+1}: Upper={upper_bband[i]}, Mid={mid_bband[i]}, Lower={lower_bband[i]}")
