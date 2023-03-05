class BaseOrder:
    def __init__(self, symbol, quantity, order_type, order_side):
        self.symbol = symbol
        self.quantity = quantity
        self.order_type = order_type
        self.order_side = order_side

    def execute(self):
        raise NotImplementedError("execute() method must be implemented in subclass")
