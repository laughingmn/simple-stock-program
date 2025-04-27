from typing import Dict

from src.models.stock import Stock
from src.utils.logger import logger


class StockService:
    """Service for managing stock information."""

    def __init__(self):
        self._stocks: Dict[str, Stock] = {}

    def add_stock(self, stock: Stock) -> None:
        """
        Add a stock to the system.
        """
        self._stocks[stock.symbol] = stock
        logger.info(f"Added stock: {stock.symbol}")

    def has_stock(self, symbol: str) -> bool:
        """
        Check if a stock exists.

        Returns:
            bool: True if stock exists, False otherwise.
        """
        return symbol in self._stocks

    def dividend_yield(self, symbol: str, price: float) -> float:
        """
        Calculate dividend yield for a stock.

        """
        stock = self._get_stock(symbol)
        return stock.dividend_yield(price)

    def pe_ratio(self, symbol: str, price: float) -> float:
        """
        Calculate price/earnings (P/E) ratio for a stock.

        """
        stock = self._get_stock(symbol)
        return stock.pe_ratio(price)

    def _get_stock(self, symbol: str) -> Stock:
        if symbol not in self._stocks:
            logger.error(f"Stock {symbol} not found.")
            raise ValueError(f"Stock {symbol} not found.")
        return self._stocks[symbol]
