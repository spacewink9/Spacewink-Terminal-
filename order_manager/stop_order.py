from order_manager.base_order import BaseOrder


class StopOrder(BaseOrder):
    def __init__(self, symbol, quantity, stop_price, side):
        super().__init__(symbol, quantity, side)
        self.stop_price = stop_price

    def execute(self):
        print(f"Executing stop {self.side} order for {self.symbol} with quantity {self.quantity} at stop price {self.stop_price}")
        # Add logic here to execute the stop order

    def cancel(self):
        print(f"Cancelling stop {self.side} order for {self.symbol} with quantity {self.quantity} at stop price {self.stop_price}")
        # Add logic here to cancel the stop order
