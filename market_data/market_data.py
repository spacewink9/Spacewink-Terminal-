from typing import List
from .bar import Bar

class MarketData:
    def __init__(self, symbol: str, bars: List[Bar]):
        self.symbol = symbol
        self.bars = bars

    def __str__(self):
        return f"Market Data for {self.symbol}:\n" + "\n".join([str(bar) for bar in self.bars])
