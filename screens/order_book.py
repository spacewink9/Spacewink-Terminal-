from screens.base_screen import BaseScreen
from market_data.market_data import MarketData

class OrderBookScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Order Book Screen ===")
        symbol = self.get_user_input("Enter symbol to view order book: ")

        # Get order book for symbol
        order_book = self.market_data.get_order_book(symbol)

        # Display bids
        print(f"\nBids for {symbol}:")
        for i in range(min(10, len(order_book.bids))):
            bid = order_book.bids[i]
            print(f"Price: {bid.price} | Size: {bid.size} | Total: {bid.total}")

        # Display asks
        print(f"\nAsks for {symbol}:")
        for i in range(min(10, len(order_book.asks))):
            ask = order_book.asks[i]
            print(f"Price: {ask.price} | Size: {ask.size} | Total: {ask.total}")
