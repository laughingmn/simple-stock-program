from dataclasses import dataclass
from datetime import datetime

from src.utils.trade_indicator import TradeIndicator


@dataclass
class Trade:
    """
    Represents a Trade record.
    """

    symbol: str
    quantity: int
    indicator: TradeIndicator  # 'buy' or 'sell'
    price: float
    timestamp: datetime
