from typing import List, Dict
from trading.order import Order


class Orderbook:
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def remove_order(self, order_id: int):
        for order in self.orders:
            if order.id == order_id:
                self.orders.remove(order)
                break

    def get_order_by_id(self, order_id: int) -> Order:
        for order in self.orders:
            if order.id == order_id:
                return order

    def get_open_orders(self) -> List[Order]:
        open_orders = []
        for order in self.orders:
            if order.status == "OPEN":
                open_orders.append(order)
        return open_orders

    def get_executed_orders(self) -> List[Order]:
        executed_orders = []
        for order in self.orders:
            if order.status == "EXECUTED":
                executed_orders.append(order)
        return executed_orders

    def get_orderbook_summary(self) -> Dict:
        open_orders = self.get_open_orders()
        executed_orders = self.get_executed_orders()

        summary = {
            "num_open_orders": len(open_orders),
            "num_executed_orders": len(executed_orders),
            "total_order_value": sum([order.value for order in self.orders]),
            "total_executed_value": sum([order.executed_value for order in executed_orders]),
        }

        return summary

    def execute_order(self, order: Order):
        # Execute order logic here
        order.execute()
