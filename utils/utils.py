import os
import sys
from datetime import datetime


def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def get_input(message, data_type=str):
    """Gets input from the user with the specified message and data type."""
    while True:
        try:
            user_input = data_type(input(message))
            break
        except ValueError:
            print(f"Invalid input. Please enter a valid {data_type.__name__}.")
    return user_input


def get_current_time():
    """Returns the current time as a string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_path(filename):
    """Returns the full path of the specified filename."""
    return os.path.join(os.path.dirname(sys.argv[0]), filename)


def format_currency(amount):
    """Formats the specified amount as a currency."""
    return "${:,.2f}".format(amount)
