import os
from datetime import datetime
from termcolor  colored

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
import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("How can I assist you with your trades?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def analyze_stock(stock_name):
    # perform analysis of the stock and return a recommendation
    recommendation = random.choice(["Buy", "Hold", "Sell"])
    return recommendation

def open_trading_website():
    # open a trading website
    webbrowser.open('https://www.tradingwebsite.com')

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'analyze stock' in query:
            speak("Which stock do you want to analyze?")
            stock_name = takeCommand().lower()
            recommendation = analyze_stock(stock_name)
            speak(f"My recommendation for {stock_name} is to {recommendation}")
        
        elif 'open trading website' in query:
            speak("Opening the trading website")
            open_trading_website()

        elif 'exit' in query:
            speak("Goodbye!")
            break
