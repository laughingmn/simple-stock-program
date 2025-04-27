from collections import defaultdict
from datetime import datetime, timedelta
from typing import Dict, List

from src.models.trade import Trade
from src.services.stock_service import StockService
from src.utils.logger import logger
from src.utils.trade_indicator import TradeIndicator


class TradeService:
    """Service for handling trades."""

    def __init__(self, stock_service: StockService):
        self._stock_service = stock_service
        self._trades_by_symbol: Dict[str, List[Trade]] = defaultdict(list)
        self._latest_trade_price: Dict[str, float] = {}

    def record_trade(
        self, symbol: str, quantity: int, indicator: TradeIndicator, price: float, timestamp: datetime = None
    ) -> None:
        """
        Record a new trade for a stock symbol.

        """
        if not self._stock_service.has_stock(symbol):
            logger.error(f"Cannot record trade. Stock {symbol} not found.")
            raise ValueError(f"Stock {symbol} not found.")

        if timestamp is None:
            timestamp = datetime.now()

        trade = Trade(
            symbol=symbol,
            quantity=quantity,
            indicator=indicator,
            price=price,
            timestamp=timestamp,
        )
        self._trades_by_symbol[symbol].append(trade)
        self._latest_trade_price[symbol] = price

    def get_trades_in_last_minutes(self, symbol: str, minutes: int = 15) -> List[Trade]:
        """
        Fetch trades for a stock symbol within the last `minutes`.

        """
        if not self._stock_service.has_stock(symbol):
            logger.error(f"Cannot fetch trades. Stock {symbol} not found.")
            raise ValueError(f"Stock {symbol} not found.")

        trades = self._trades_by_symbol.get(symbol, [])
        cutoff_time = datetime.now() - timedelta(minutes=minutes)
        return [trade for trade in trades if trade.timestamp >= cutoff_time]

    def volume_weighted_stock_price(self, symbol: str, minutes: int = 15) -> float:
        """
        Calculate the volume-weighted stock price for a stock symbol.

        Returns:
            float: volume-weighted price, or 0.0 if no trades.
        """
        trades = self.get_trades_in_last_minutes(symbol, minutes)
        if not trades:
            logger.warning(f"No trades found for {symbol} in last {minutes} minutes.")
            return 0.0

        total_trade_price_quantity = sum(trade.price * trade.quantity for trade in trades)
        total_quantity = sum(trade.quantity for trade in trades)

        return total_trade_price_quantity / total_quantity

    def geometric_mean(self) -> float:
        """
        Calculate the GBCE All Share Index using the geometric mean of latest trade prices.

        Returns:
            float: geometric mean, or 0.0 if no trades.
        """

        prices = list(self._latest_trade_price.values())
        num_prices = len(prices)

        if num_prices == 0:
            logger.warning("No trades recorded for geometric mean calculation.")
            return 0.0

        product = 1.0
        for price in prices:
            product *= price

        return product ** (1 / num_prices)
