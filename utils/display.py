def print_table(headers, data):
    """Prints a formatted table to the console.

    Args:
        headers (list): A list of strings containing the column headers.
        data (list of lists): A list of lists containing the table data.
    """
    # Calculate the maximum width of each column
    column_widths = [len(header) for header in headers]
    for row in data:
        for i, value in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(value)))

    # Print the table header
    print('|'.join(header.ljust(column_widths[i]) for i, header in enumerate(headers)))

    # Print the separator row
    separator = '+'.join('-' * column_widths[i] for i in range(len(headers)))
    print(separator)

    # Print the table data
    for row in data:
        print('|'.join(str(value).ljust(column_widths[i]) for i, value in enumerate(row)))


def print_menu(title, options):
    """Prints a formatted menu to the console.

    Args:
        title (str): The title of the menu.
        options (list): A list of tuples containing the menu options.
            Each tuple contains two strings: the option text and the option value.
    """
    print(title)
    for option in options:
        print(f'{option[0]}. {option[1]}')
print()

# Prompt user to enter their choice
choice = input("Enter your choice: ")

# Clear the screen
clear_screen()

# Call the corresponding function based on user choice
if choice == "1":
    stock_quote()
elif choice == "2":
    stock_chart()
elif choice == "3":
    stock_news()
elif choice == "4":
    stock_info()
elif choice == "5":
    stock_options()
elif choice == "6":
    stock_dividend()
elif choice == "7":
    stock_recommendations()
elif choice == "8":
    stock_historical_data()
elif choice == "9":
    crypto_quote()
elif choice == "10":
    crypto_chart()
elif choice == "11":
    crypto_news()
elif choice == "12":
    forex_quote()
elif choice == "13":
    forex_chart()
elif choice == "14":
    forex_news()
elif choice == "15":
    economic_calendar()
elif choice == "16":
    trades_submenu()
elif choice == "17":
    fundamental_analysis_submenu()
elif choice == "18":
    # Exit the program
    print("Thank you for using Spacewink Terminal!")
    sys.exit()
else:
    print("Invalid choice. Please try again.")
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")
