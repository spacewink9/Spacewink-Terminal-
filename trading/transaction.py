from typing import Optional
from datetime import datetime

class Transaction:
    """A class to represent a transaction."""

    def __init__(self, symbol: str, quantity: float, price: float, side: str, timestamp: Optional[datetime] = None):
        """
        Initialize the Transaction object.

        Parameters
        ----------
        symbol : str
            The symbol of the security being transacted.
        quantity : float
            The quantity of shares or contracts transacted.
        price : float
            The price at which the transaction occurred.
        side : str
            The side of the transaction, either 'buy' or 'sell'.
        timestamp : datetime, optional
            The timestamp of the transaction, default is the current date and time.
        """
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.side = side
        self.timestamp = timestamp or datetime.now()

    @property
    def cost(self) -> float:
        """Return the total cost of the transaction."""
        return self.quantity * self.price

    def __repr__(self):
        return f"{self.timestamp}: {self.side.upper()} {self.quantity} {self.symbol} @ {self.price:.2f}"
