from utils.log import setup_logging
from utils.display import clear_screen, show_header
from screens.trades import TradesScreen
from screens.valuation_analysis import ValuationAnalysisScreen
from screens.fundamental_analysis import FundamentalAnalysisScreen


class SpacewinkTerminal:
    def __init__(self):
        setup_logging()
        self.screens = [
            TradesScreen(),
            ValuationAnalysisScreen(),
            FundamentalAnalysisScreen()
        ]

    def run(self):
        while True:
            clear_screen()
            show_header()

            for i, screen in enumerate(self.screens):
                print(f"{i + 1}. {screen.name}")

            print("\n0. Exit\n")

            choice = input("Enter your choice: ")
            clear_screen()

            try:
                choice = int(choice)
            except ValueError:
                print("Invalid choice. Please enter a number.")
                continue

            if choice == 0:
                print("Thank you for using Spacewink Terminal!")
                break

            try:
                self.screens[choice - 1].run()
            except IndexError:
                print("Invalid choice. Please try again.")
                continue
