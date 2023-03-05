from screens.base_screen import BaseScreen
from order_manager.stop_order import StopOrder

class SelectStopTypeScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)

    def display(self):
        self.clear_screen()
        print("=== Select Stop Type Screen ===")

        # Prompt user to select stop type
        stop_type = self.get_user_choice("Select stop type:", ["Stop loss", "Trailing stop"])
        if stop_type == "Stop loss":
            self.display_stop_loss()
        elif stop_type == "Trailing stop":
            self.display_trailing_stop()

    def display_stop_loss(self):
        self.clear_screen()
        print("=== Stop Loss Screen ===")

        # Prompt user to enter stop price
        stop_price = self.get_user_input_float("Enter stop price: ")

        # Create stop order and return to previous screen
        stop_order = StopOrder(stop_price)
        self.terminal.set_active_screen(self.terminal.previous_screen)

    def display_trailing_stop(self):
        self.clear_screen()
        print("=== Trailing Stop Screen ===")

        # Prompt user to enter trailing stop distance
        trailing_distance = self.get_user_input_float("Enter trailing distance: ")

        # Create stop order and return to previous screen
        stop_order = StopOrder(trailing_distance=trailing_distance)
        self.terminal.set_active_screen(self.terminal.previous_screen)
