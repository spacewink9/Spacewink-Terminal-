import os
from datetime import datetime
from termcolor import colored

def show_trades_menu():
    os.system('clear')
    print(colored('SPACEWINK TERMINAL - TRADES MENU', 'green'))
    print('\n')
    print('1. Place Buy Order')
    print('2. Place Sell Order')
    print('3. View Open Orders')
    print('4. View Trade History')
    print('5. Go back to Main Menu')
    print('\n')

def place_buy_order():
    os.system('clear')
    print(colored('SPACEWINK TERMINAL - PLACE BUY ORDER', 'green'))
    print('\n')
    print('Enter the following details to place a buy order:')
    symbol = input('Symbol: ')
    amount = float(input('Amount: '))
    price = float(input('Price: '))
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('\n')
    print(f'Buy Order placed successfully at {date_time}')
    print(f'Symbol: {symbol}')
    print(f'Amount: {amount}')
    print(f'Price: {price}')

def place_sell_order():
    os.system('clear')
    print(colored('SPACEWINK TERMINAL - PLACE SELL ORDER', 'green'))
    print('\n')
    print('Enter the following details to place a sell order:')
    symbol = input('Symbol: ')
    amount = float(input('Amount: '))
    price = float(input('Price: '))
    date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('\n')
    print(f'Sell Order placed successfully at {date_time}')
    print(f'Symbol: {symbol}')
    print(f'Amount: {amount}')
    print(f'Price: {price}')

def view_open_orders():
    os.system('clear')
    print(colored('SPACEWINK TERMINAL - OPEN ORDERS', 'green'))
    print('\n')
    print('You have no open orders.')

def view_trade_history():
    os.system('clear')
    print(colored('SPACEWINK TERMINAL - TRADE HISTORY', 'green'))
    print('\n')
    print('You have no trade history.')

def trades_main():
    while True:
        show_trades_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            place_buy_order()
            input('\nPress Enter to continue...')
        elif choice == '2':
            place_sell_order()
            input('\nPress Enter to continue...')
        elif choice == '3':
            view_open_orders()
            input('\nPress Enter to continue...')
        elif choice == '4':
            view_trade_history()
            input('\nPress Enter to continue...')
        elif choice == '5':
            break
        else:
            print(colored('Invalid choice. Please try again.', 'red'))
            input('\nPress Enter to continue...')
