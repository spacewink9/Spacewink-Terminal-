from screens.base_screen import BaseScreen
from order_manager.order_manager import OrderManager
from market_data.market_data import MarketData

class OrdersScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.order_manager = OrderManager()
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Orders Screen ===")
        symbol = self.get_user_input("Enter symbol to view orders for: ")
        orders = self.order_manager.get_orders_for_symbol(symbol)

        if not orders:
            print(f"No orders found for {symbol}.")
        else:
            print(f"\nAll orders for {symbol}:")
            for order in orders:
                print(order)

            # Get current market price
            current_price = self.market_data.get_latest_bar(symbol).close_price

            # Calculate unrealized P&L for each order
            print(f"\nUnrealized P&L for each order:")
            for order in orders:
                if order.is_buy:
                    pnl = (current_price - order.price) * order.quantity
                else:
                    pnl = (order.price - current_price) * order.quantity
                print(f"{order.order_id}: {pnl}")

            # Calculate total unrealized P&L
            total_pnl = sum((current_price - order.price) * order.quantity if order.is_buy else (order.price - current_price) * order.quantity for order in orders)
            print(f"\nTotal unrealized P&L: {total_pnl}")
