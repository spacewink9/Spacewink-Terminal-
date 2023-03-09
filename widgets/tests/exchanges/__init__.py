"""
This module provides tests for exchanges.
"""

from . import test_binance
from . import test_coinbase
from . import test_kraken

__all__ = [
    "test_binance",
    "test_coinbase",
    "test_kraken"
]
