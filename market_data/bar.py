class Bar:
    def __init__(self, symbol, timestamp, open_price, high_price, low_price, close_price, volume):
        self.symbol = symbol
        self.timestamp = timestamp
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume

    def __str__(self):
        return f"{self.symbol}: {self.timestamp} | Open: {self.open_price}, High: {self.high_price}, Low: {self.low_price}, Close: {self.close_price}, Volume: {self.volume}"
