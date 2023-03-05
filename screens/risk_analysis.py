from screens.base_screen import BaseScreen
from market_data.market_data import MarketData
from indicators.atr import ATR

class RiskAnalysisScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Risk Analysis Screen ===")
        symbol = self.get_user_input("Enter symbol to analyze: ")

        # Get market data for symbol
        bars = self.market_data.get_latest_bars(symbol, 100)
        high_prices = [bar.high_price for bar in bars]
        low_prices = [bar.low_price for bar in bars]
        close_prices = [bar.close_price for bar in bars]

        # Calculate ATR
        atr = ATR(high_prices, low_prices, close_prices, 14)
        atr_values = atr.calculate()

        # Calculate average ATR
        avg_atr = sum(atr_values) / len(atr_values)

        # Calculate risk based on current price
        current_price = bars[-1].close_price
        stop_loss = current_price - (2 * avg_atr)
        target_price = current_price + (3 * avg_atr)
        risk_reward_ratio = (target_price - current_price) / (current_price - stop_loss)

        # Display results
        print(f"\nLatest {len(bars)} bars for {symbol}:")
        for bar in bars:
            print(bar)

        print(f"\nATR values for {symbol}:")
        for i in range(len(atr_values)):
            print(f"Bar {i+1}: {atr_values[i]}")

        print(f"\nAverage ATR for {symbol}: {avg_atr:.2f}")
        print(f"Current price for {symbol}: {current_price:.2f}")
        print(f"Stop loss for {symbol}: {stop_loss:.2f}")
        print(f"Target price for {symbol}: {target_price:.2f}")
        print(f"Risk/reward ratio for {symbol}: {risk_reward_ratio:.2f}")
