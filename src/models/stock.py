from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Stock(ABC):
    symbol: str
    last_dividend: float
    par_value: float

    @abstractmethod
    def dividend_yield(self, price: float) -> float:
        """Calculate dividend yield"""
        pass

    def pe_ratio(self, price: float) -> float:
        """Calculate P/E Ratio"""
        if self.last_dividend == 0:
            return 0
        return price / self.last_dividend


@dataclass
class CommonStock(Stock):
    def dividend_yield(self, price: float) -> float:
        return self.last_dividend / price


@dataclass
class PreferredStock(Stock):
    fixed_dividend: float

    def dividend_yield(self, price: float) -> float:
        return (self.fixed_dividend * self.par_value) / price
