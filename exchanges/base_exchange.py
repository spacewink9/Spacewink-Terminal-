from abc import ABC, abstractmethod
from typing import List, Tuple

class BaseExchange(ABC):
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    @abstractmethod
    def get_markets(self) -> List[str]:
        pass

    @abstractmethod
    def get_orderbook(self, market: str) -> Tuple[List[Tuple[float, float]], List[Tuple[float, float]]]:
        pass

    @abstractmethod
    def get_ticker(self, market: str) -> Tuple[float, float]:
        pass

    @abstractmethod
    def get_trades(self, market: str) -> List[Tuple[float, float]]:
        pass

    @abstractmethod
    def place_limit_order(self, market: str, quantity: float, price: float, side: str) -> str:
        pass

    @abstractmethod
    def cancel_order(self, order_id: str) -> bool:
        pass

    @abstractmethod
    def get_order_status(self, order_id: str) -> str:
        pass

    @abstractmethod
    def get_open_orders(self, market: str = None) -> List[Dict]:
        pass

    @abstractmethod
    def get_order_history(self, market: str = None) -> List[Dict]:
        pass

    @abstractmethod
    def get_balances(self) -> Dict[str, float]:
        pass

    @abstractmethod
    def get_trade_history(self, market: str = None) -> List[Dict]:
        pass
