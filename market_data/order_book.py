class OrderBook:
    def __init__(self, bids=None, asks=None):
        self.bids = bids if bids is not None else {}
        self.asks = asks if asks is not None else {}

    def update(self, data):
        """
        Updates the order book with new data.

        Parameters:
        - data (dict): A dictionary containing the new order book data.

        Example data format:
        {
            "bids": [
                [100.0, 10.0],
                [99.5, 5.0]
            ],
            "asks": [
                [101.0, 7.0],
                [102.0, 3.0]
            ]
        }
        """
        for bid in data.get("bids", []):
            price, quantity = bid
            if quantity == 0:
                del self.bids[price]
            else:
                self.bids[price] = quantity
        for ask in data.get("asks", []):
            price, quantity = ask
            if quantity == 0:
                del self.asks[price]
            else:
                self.asks[price] = quantity

    def get_bid_ask_spread(self):
        """
        Returns the bid-ask spread (difference between the best bid and best ask).
        """
        best_bid = max(self.bids.keys()) if self.bids else None
        best_ask = min(self.asks.keys()) if self.asks else None
        return best_ask - best_bid if best_bid and best_ask else None

    def get_mid_price(self):
        """
        Returns the mid price (average of the best bid and best ask).
        """
        best_bid = max(self.bids.keys()) if self.bids else None
        best_ask = min(self.asks.keys()) if self.asks else None
        return (best_bid + best_ask) / 2 if best_bid and best_ask else None
