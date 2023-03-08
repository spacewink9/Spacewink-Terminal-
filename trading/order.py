from typing import Union


class Order:
    def __init__(
        self,
        symbol: str,
        qty: int,
        order_type: str,
        price: Union[None, float] = None,
        time_in_force: str = "GTC",
    ):
        self.symbol = symbol
        self.qty = qty
        self.order_type = order_type
        self.price = price
        self.time_in_force = time_in_force

    def execute(self):
        """Execute the order."""
        # code for executing the order goes here
        pass

    def cancel(self):
        """Cancel the order."""
        # code for canceling the order goes here
        pass

    def update_price(self, price: float):
        """Update the price of the order."""
        self.price = price

    def update_qty(self, qty: int):
        """Update the quantity of the order."""
        self.qty = qty

    def to_dict(self):
        """Return the order as a dictionary."""
        return {
            "symbol": self.symbol,
            "qty": self.qty,
            "order_type": self.order_type,
            "price": self.price,
            "time_in_force": self.time_in_force,
        }
