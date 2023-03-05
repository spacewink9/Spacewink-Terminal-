import time
from screens.base_screen import BaseScreen
from screens.select_exchange import SelectExchangeScreen
from screens.select_market import SelectMarketScreen
from screens.select_order_type import SelectOrderTypeScreen
from screens.select_stop_type import SelectStopTypeScreen
from screens.select_position import SelectPositionScreen
from order_manager.order_manager import OrderManager
from market_data.market_data import MarketData
from indicators.rsi import RSI
from indicators.macd import MACD

class TerminalScreen(BaseScreen):
    def __init__(self, terminal):
        super().__init__(terminal)
        self.order_manager = OrderManager()
        self.market_data = MarketData()

    def display(self):
        self.clear_screen()
        print("=== Spacewink Terminal ===")
        print("1. View market data")
        print("2. Place an order")
        print("3. Exit")

        choice = self.get_user_input("Enter your choice: ")

        if choice == "1":
            self.display_market_data_menu()
        elif choice == "2":
            self.display_order_menu()
        elif choice == "3":
            self.exit_terminal()

    def display_market_data_menu(self):
        self.clear_screen()
        print("=== Market Data ===")
        print("1. Select exchange")
        print("2. Select market")
        print("3. View technical indicators")
        print("4. Back")

        choice = self.get_user_input("Enter your choice: ")

        if choice == "1":
            self.display_select_exchange_screen()
        elif choice == "2":
            self.display_select_market_screen()
        elif choice == "3":
            self.display_technical_indicators_menu()
        elif choice == "4":
            self.display()

    def display_select_exchange_screen(self):
        select_exchange_screen = SelectExchangeScreen(self.terminal)
        select_exchange_screen.display()

    def display_select_market_screen(self):
        select_market_screen = SelectMarketScreen(self.terminal)
        select_market_screen.display()

    def display_technical_indicators_menu(self):
        self.clear_screen()
        print("=== Technical Indicators ===")
        print("1. Relative Strength Index (RSI)")
        print("2. Moving Average Convergence Divergence (MACD)")
        print("3. Back")

        choice = self.get_user_input("Enter your choice: ")

        if choice == "1":
            self.display_rsi_chart()
        elif choice == "2":
            self.display_macd_chart()
        elif choice == "3":
            self.display_market_data_menu()

    def display_rsi_chart(self):
        self.clear_screen()
        print("=== Relative Strength Index (RSI) ===")
        symbol = self.get_user_input("Enter symbol to analyze: ")
        bars = self.market_data.get_latest_bars(symbol, 14)
        close_prices = [bar.close_price for bar in bars]
        rsi = RSI(close_prices)
        rsi_values = rsi.calculate()
        print(f"RSI values for {symbol}:")
        for i in range(len(rsi_values)):
            print(f"Bar {i+1}: {rsi_values[i]}")
        time.sleep(5)

    def display_macd_chart(self):
        self.clear_screen()
        print("=== Moving Average Convergence Divergence (MACD) ===")
        symbol = self.get_user_input("Enter symbol to analyze: ")
        bars = self.market_data.get_latest_bars(symbol, 26)
        close_prices = [bar.close_price for bar in bars]
        macd = MACD(close_prices)
        macd_values = macd.calculate_macd()
            # Print the MACD values
    print("MACD:", macd_values)

    # Calculate the Signal Line values
    signal_line = macd.calculate_signal_line()

    # Print the Signal Line values
    print("Signal Line:", signal_line)

    # Plot the MACD and Signal Line
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(candles.index, macd_values, label='MACD')
    ax.plot(candles.index, signal_line, label='Signal Line')
    ax.legend()
    ax.set(title='MACD and Signal Line', xlabel='Date', ylabel='Price')
    plt.show()

def get_rsi(self, symbol, interval):
    """
    Calculate and plot the Relative Strength Index (RSI) for the specified symbol and interval.
    """
    # Get the candles for the specified symbol and interval
    candles = self.market_data.get_candles(symbol=symbol, interval=interval)

    # Create an RSI object
    rsi = RSI(candles=candles)

    # Calculate the RSI values
    rsi_values = rsi.calculate_rsi()

    # Print the RSI values
    print("RSI:", rsi_values)

    # Plot the RSI values
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(candles.index, rsi_values, label='RSI')
    ax.axhline(y=30, color='red', linestyle='--')
    ax.axhline(y=70, color='red', linestyle='--')
    ax.legend()
    ax.set(title='RSI', xlabel='Date', ylabel='RSI Value')
    plt.show()

def get_bollinger_bands(self, symbol, interval):
    """
    Calculate and plot the Bollinger Bands for the specified symbol and interval.
    """
    # Get the candles for the specified symbol and interval
    candles = self.market_data.get_candles(symbol=symbol, interval=interval)

    # Create a BollingerBands object
    bbands = BollingerBands(candles=candles)

    # Calculate the Bollinger Bands values
    upper_band, middle_band, lower_band = bbands.calculate_bollinger_bands()

    # Print the Bollinger Bands values
    print("Upper Band:", upper_band)
    print("Middle Band:", middle_band)
    print("Lower Band:", lower_band)

    # Plot the Bollinger Bands values
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(candles.index, upper_band, label='Upper Band')
    ax.plot(candles.index, middle_band, label='Middle Band')
    ax.plot(candles.index, lower_band, label='Lower Band')
    ax.fill_between(candles.index, upper_band, lower_band, alpha=0.2)
    ax.legend()
    ax.set(title='Bollinger Bands', xlabel='Date', ylabel='Price')
    plt.show()

