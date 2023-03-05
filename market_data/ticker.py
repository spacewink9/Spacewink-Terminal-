class Ticker:
    def __init__(self, symbol, last_price, bid_price, bid_size, ask_price, ask_size):
        self.symbol = symbol
        self.last_price = last_price
        self.bid_price = bid_price
        self.bid_size = bid_size
        self.ask_price = ask_price
        self.ask_size = ask_size

    def __str__(self):
        return f"{self.symbol}: Last Price: {self.last_price}, Bid Price: {self.bid_price}, Bid Size: {self.bid_size}, Ask Price: {self.ask_price}, Ask Size: {self.ask_size}"
