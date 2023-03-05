from screens.base_screen import BaseScreen
from utils.config import Config


class ExchangeInfoScreen(BaseScreen):
    def __init__(self, exchange_name):
        super().__init__("Exchange Information")

        self.exchange_name = exchange_name
        self.config = Config()

    def display(self):
        super().display()

        print(f"Exchange Name: {self.exchange_name}")
        print("")

        print("Exchange Settings:")
        print("-------------------")
        print("1. Enable/Disable API logging")
        print("2. Enable/Disable order book data")
        print("3. Enable/Disable market data streaming")
        print("4. Enable/Disable voice alerts")
        print("5. Set trading bot parameters")
        print("6. Return to previous menu")
        print("")

        choice = input("Enter an option: ")
        if choice == "1":
            self.toggle_api_logging()
        elif choice == "2":
            self.toggle_order_book_data()
        elif choice == "3":
            self.toggle_market_data_streaming()
        elif choice == "4":
            self.toggle_voice_alerts()
        elif choice == "5":
            self.set_trading_bot_parameters()
        elif choice == "6":
            self.previous_menu()
        else:
            print("Invalid option. Please try again.")
            self.display()

    def toggle_api_logging(self):
        api_logging_enabled = self.config.get("api_logging_enabled", False)

        if api_logging_enabled:
            self.config.set("api_logging_enabled", False)
            print("API logging disabled.")
        else:
            self.config.set("api_logging_enabled", True)
            print("API logging enabled.")

        self.config.save()

    def toggle_order_book_data(self):
        order_book_data_enabled = self.config.get("order_book_data_enabled", False)

        if order_book_data_enabled:
            self.config.set("order_book_data_enabled", False)
            print("Order book data disabled.")
        else:
            self.config.set("order_book_data_enabled", True)
            print("Order book data enabled.")

        self.config.save()

    def toggle_market_data_streaming(self):
        market_data_streaming_enabled = self.config.get("market_data_streaming_enabled", False)

        if market_data_streaming_enabled:
            self.config.set("market_data_streaming_enabled", False)
            print("Market data streaming disabled.")
        else:
            self.config.set("market_data_streaming_enabled", True)
            print("Market data streaming enabled.")

        self.config.save()

    def toggle_voice_alerts(self):
        voice_alerts_enabled = self.config.get("voice_alerts_enabled", False)

        if voice_alerts_enabled:
            self.config.set("voice_alerts_enabled", False)
            print("Voice alerts disabled.")
        else:
            self.config.set("voice_alerts_enabled", True)
            print("Voice alerts enabled.")

        self.config.save()

    def set_trading_bot_parameters(self):
        print("Trading bot parameters set.")
        # TODO: Add implementation for setting trading bot parameters

    def previous_menu(self):
        # TODO: Add implementation for returning to previous menu
        pass
