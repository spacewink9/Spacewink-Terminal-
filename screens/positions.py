from screens.base_screen import BaseScreen
from order_manager.order_manager import OrderManager
from utils.api import get_account_balance, get_open_positions

class PositionsScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.order_manager = OrderManager()
    
    def display(self):
        self.clear_screen()
        print("=== Positions Screen ===")

        # Get account balance
        account_balance = get_account_balance()
        print(f"Account Balance: {account_balance}")

        # Get open positions
        open_positions = get_open_positions()
        if not open_positions:
            print("\nYou currently have no open positions.")
            return
        
        # Display open positions
        print("\nOpen Positions:")
        for position in open_positions:
            print(f"\nSymbol: {position['symbol']}")
            print(f"Size: {position['size']}")
            print(f"Entry Price: {position['entry_price']}")
            print(f"Current Price: {position['current_price']}")
            print(f"Unrealized P/L: {position['unrealized_pl']}")
            print(f"Margin Used: {position['margin_used']}")
            print(f"Leverage: {position['leverage']}")
            print(f"Isolated Margin: {position['isolated_margin']}")
            print(f"Position Type: {position['position_type']}")
            print(f"Is Cross Margin: {position['is_cross_margin']}")
            print(f"Creation Time: {position['creation_time']}")

        # Ask user if they want to close any positions
        response = self.get_user_input("\nDo you want to close any positions? (y/n) ")
        if response.lower() == "y":
            symbol = self.get_user_input("Enter symbol of position to close: ")
            size = self.get_user_input("Enter size of position to close: ")
            order = self.order_manager.create_market_order(symbol, size, "sell")
            self.order_manager.execute_order(order)
            print(f"\nSuccessfully closed position: {symbol} {size}")
