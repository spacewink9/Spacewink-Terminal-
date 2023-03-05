from screens.base_screen import BaseScreen

class SelectExchangeScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.exchanges = ["Binance", "Coinbase Pro", "Kraken", "FTX"]

    def display(self):
        self.clear_screen()
        print("=== Select Exchange Screen ===")
        print("Available exchanges:")
        for i, exchange in enumerate(self.exchanges):
            print(f"{i+1}. {exchange}")

        selected_index = self.get_user_input_int("Enter exchange number: ", 1, len(self.exchanges))
        selected_exchange = self.exchanges[selected_index - 1]

        print(f"\nSelected exchange: {selected_exchange}")
        return selected_exchange
