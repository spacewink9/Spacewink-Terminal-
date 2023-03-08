from typing import List, Dict
import pandas as pd

from trading.portfolio import Portfolio
from trading.order import Order
from trading.execution import ExecutionHandler


class TradingAlgorithm:
    """
    The TradingAlgorithm class encapsulates a set of instructions that determine how trading orders should be
    placed and executed. It uses a portfolio object to keep track of its positions and values, and an execution
    handler object to handle the actual placing of orders with a broker.
    """
    def __init__(self, portfolio: Portfolio, execution_handler: ExecutionHandler):
        self.portfolio = portfolio
        self.execution_handler = execution_handler

    def on_bar(self, data: Dict[str, pd.DataFrame]):
        """
        The on_bar method is called each time new market data is available. It should be implemented in a subclass
        to define the trading logic that will be executed based on the latest data.

        Parameters
        ----------
        data : Dict[str, pd.DataFrame]
            A dictionary containing DataFrames with market data for each symbol being traded.
        """
        raise NotImplementedError("on_bar method not implemented")

    def on_order(self, order: Order):
        """
        The on_order method is called each time a new order is placed. It should be implemented in a subclass
        to define any logic that should be executed when an order is placed.

        Parameters
        ----------
        order : Order
            The Order object representing the order that was placed.
        """
        pass

    def on_execution(self, execution):
        """
        The on_execution method is called each time a new execution report is received from the broker. It should be
        implemented in a subclass to define any logic that should be executed when an execution report is received.

        Parameters
        ----------
        execution : Execution
            The Execution object representing the execution report received from the broker.
        """
        pass

    def on_fill(self, fill):
        """
        The on_fill method is called each time a new fill report is received from the broker. It should be
        implemented in a subclass to define any logic that should be executed when a fill report is received.

        Parameters
        ----------
        fill : Fill
            The Fill object representing the fill report received from the broker.
        """
        pass

    def on_tick(self, data: Dict[str, pd.DataFrame]):
        """
        The on_tick method is called each time a new tick is available. It should be implemented in a subclass
        to define the trading logic that will be executed based on the latest tick.

        Parameters
        ----------
        data : Dict[str, pd.DataFrame]
            A dictionary containing DataFrames with market data for each symbol being traded.
        """
        raise NotImplementedError("on_tick method not implemented")

    def run(self, data: Dict[str, pd.DataFrame], events: List[str]):
        """
        The run method is the main method that is called to start the trading algorithm. It loops through the
        events provided and calls the corresponding method to handle each event.

        Parameters
        ----------
        data : Dict[str, pd.DataFrame]
            A dictionary containing DataFrames with market data for each symbol being traded.
        events : List[str]
            A list of event types to process (e.g. "BAR", "TICK", etc.).
        """
        for event in events:
            if event == "BAR":
                self.on_bar(data)
            elif event == "TICK":
                self.on_tick(data)
            elif event == "ORDER":
                self.on_order(data)
            elif event == "EXECUTION":
                self.on_execution(data)
            elif event == "FILL":
                self.on_fill(data)
            else:
                raise ValueError(f"Invalid event type: {event}")
