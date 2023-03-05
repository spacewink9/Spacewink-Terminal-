from .base_order import BaseOrder

class OrderManager:
    def __init__(self):
        self.orders = []

    def add_order(self, order: BaseOrder):
        self.orders.append(order)

    def remove_order(self, order: BaseOrder):
        self.orders.remove(order)

    def get_orders(self):
        return self.orders
