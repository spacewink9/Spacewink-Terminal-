class Trade:
    def __init__(self, symbol, timestamp, price, volume, side):
        self.symbol = symbol
        self.timestamp = timestamp
        self.price = price
        self.volume = volume
        self.side = side

    def __str__(self):
        return f"{self.symbol}: {self.timestamp} | Price: {self.price}, Volume: {self.volume}, Side: {self.side}"
