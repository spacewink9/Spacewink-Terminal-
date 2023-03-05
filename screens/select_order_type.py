from screens.base_screen import BaseScreen

class SelectOrderTypeScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)

    def display(self):
        self.clear_screen()
        print("=== Select Order Type Screen ===")
        print("1. Limit Order")
        print("2. Market Order")
        print("3. Stop Order")
        print("4. Cancel Order")
        print("0. Back to previous screen")
        choice = self.get_user_input("Enter choice: ")

        if choice == "1":
            self.terminal.set_current_screen("limit_order")
        elif choice == "2":
            self.terminal.set_current_screen("market_order")
        elif choice == "3":
            self.terminal.set_current_screen("stop_order")
        elif choice == "4":
            self.terminal.set_current_screen("cancel_order")
        elif choice == "0":
            self.terminal.go_back()
        else:
            self.display_error("Invalid choice. Please try again.")
