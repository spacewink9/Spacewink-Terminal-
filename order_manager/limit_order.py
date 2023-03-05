from .base_order import BaseOrder

class LimitOrder(BaseOrder):
    def __init__(self, symbol, side, price, quantity, time_in_force='GTC'):
        super().__init__(symbol, side, time_in_force)
        self.type = 'LIMIT'
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        order = super().to_dict()
        order.update({
            'type': self.type,
            'price': self.price,
            'quantity': self.quantity
        })
        return order
