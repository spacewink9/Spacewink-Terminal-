from screens.base_screen import BaseScreen
from market_data.market_data import MarketData

class SelectMarketScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Select Market Screen ===")
        print("Available markets:")
        for market in self.market_data.get_available_markets():
            print(f"- {market}")

        selected_market = self.get_user_input("\nEnter market symbol to select: ")
        if not self.market_data.is_valid_market(selected_market):
            print("Invalid market symbol.")
            return

        self.terminal.set_selected_market(selected_market)
        print(f"Selected market: {selected_market}")
