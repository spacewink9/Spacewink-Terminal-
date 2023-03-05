import curses
import time
import traceback

from screens import *
from utils import display, log

# Initialize the logger
log.init_logger()

# Set the color pairs
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

# Define the main function
def main(stdscr):
    # Hide the cursor
    curses.curs_set(0)

    # Initialize the screen
    display.init_screen(stdscr)

    # Define the main menu options
    main_menu = [
        ["1", "Real-time Quotes"],
        ["2", "Historical Quotes"],
        ["3", "News"],
        ["4", "Financial Statements"],
        ["5", "Valuation Analysis"],
        ["6", "Trades"],
        ["7", "Technical Analysis"],
        ["8", "Options"],
        ["9", "Exit"]
    ]

    # Define the submenu options for fundamental analysis
    fundamental_analysis_submenu = [
        ["10", "Balance Sheet"],
        ["11", "Income Statement"],
        ["12", "Cash Flow Statement"],
        ["13", "Key Ratios"],
        ["14", "Financial Health"],
        ["15", "Price Multiples"],
        ["16", "Dividends"],
        ["17", "Earnings Call Transcripts"],
        ["18", "Go back to main menu"]
    ]

    # Add the submenu to the main menu
    main_menu.insert(4, ["4", "Fundamental Analysis", fundamental_analysis_submenu])

    # Define the options for the technical analysis submenu
    technical_analysis_submenu = [
        ["19", "Candlestick Chart"],
        ["20", "Moving Averages"],
        ["21", "Relative Strength Index (RSI)"],
        ["22", "Bollinger Bands"],
        ["23", "Fibonacci Retracement"],
        ["24", "Go back to main menu"]
    ]

    # Add the submenu to the main menu
    main_menu.insert(6, ["6", "Technical Analysis", technical_analysis_submenu])

    # Define the options for the options submenu
    options_submenu = [
        ["25", "Option Chain"],
        ["26", "Option Strategies"],
        ["27", "Go back to main menu"]
    ]

    # Add the submenu to the main menu
    main_menu.insert(7, ["7", "Options", options_submenu])

    # Set the initial selected option
    selected_option = 0

    # Loop until the user selects the exit option
    while selected_option != len(main_menu) - 1:
        # Clear the screen
        stdscr.clear()

        # Print the title
        display.print_title(stdscr, "Spacewink Terminal")

        # Print the menu options
        for i, option in enumerate(main_menu):
            display.print_menu_option(stdscr, option[1], i, selected_option)

        # Refresh the screen
        stdscr.refresh()

        # Get user input
        key = stdscr.getch()

        # Move the selected option based on user input
        if key == curses.KEY_UP:
            selected_option = (selected_option - 1) % len(main_menu)
        elif key == curses.KEY_DOWN:
            selected_option = (selected_option + 1) % len(main_menu)
        elif key == curses.KEY_ENTER or key in [10, 13]:
            # If the elif choice == "9":
    log_menu()
    log_choice = input("Enter choice: ")
    while log_choice != "3":
        if log_choice == "1":
            log_trade()
        elif log_choice == "2":
            log_valuation()
        else:
            print("Invalid choice. Please try again.")
        log_choice = input("Enter choice: ")
else:
    print("Invalid choice. Please try again.")
    # If the user entered an invalid choice, display an error message and loop back to the main menu
    log.write_log(f"Invalid option selected: {choice}")
    input("Press Enter to continue...")
    clear_screen()
    continue

