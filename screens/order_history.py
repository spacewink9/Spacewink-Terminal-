from screens.base_screen import BaseScreen
from order_manager.order_manager import OrderManager
from utils.display import format_currency

class OrderHistoryScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.order_manager = OrderManager()

    def display(self):
        self.clear_screen()
        print("=== Order History Screen ===")

        # Get order history
        orders = self.order_manager.get_order_history()

        # Display order history
        if orders:
            print("\nOrder History:")
            for order in orders:
                print(f"Order ID: {order.order_id}")
                print(f"Symbol: {order.symbol}")
                print(f"Side: {order.side}")
                print(f"Type: {order.type}")
                print(f"Quantity: {order.quantity}")
                print(f"Price: {format_currency(order.price, order.symbol)}")
                print(f"Status: {order.status}")
                print(f"Timestamp: {order.timestamp}")
                print("---")
        else:
            print("\nNo orders found in history.")
