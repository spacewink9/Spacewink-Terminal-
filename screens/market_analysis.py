from screens.base_screen import BaseScreen
from market_data.market_data import MarketData
from indicators.sma import SMA

class MarketAnalysisScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Market Analysis Screen ===")
        symbol = self.get_user_input("Enter symbol to analyze: ")

        # Get market data for symbol
        bars = self.market_data.get_latest_bars(symbol, 100)
        close_prices = [bar.close_price for bar in bars]

        # Calculate SMA
        sma = SMA(close_prices, 20)
        sma_values = sma.calculate()

        # Display results
        print(f"\nLatest {len(bars)} bars for {symbol}:")
        for bar in bars:
            print(bar)

        print(f"\nSMA values for {symbol}:")
        for i in range(len(sma_values)):
            print(f"Bar {i+1}: {sma_values[i]}")
