import pytest

from src.models.stock import CommonStock, PreferredStock
from src.services.stock_service import StockService
from src.services.trade_service import TradeService


@pytest.fixture
def stock_service():
    service = StockService()
    service.add_stock(CommonStock(symbol="TEA", last_dividend=0, par_value=100))
    service.add_stock(CommonStock(symbol="POP", last_dividend=8, par_value=100))
    service.add_stock(PreferredStock(symbol="GIN", last_dividend=8, fixed_dividend=0.02, par_value=100))
    return service


@pytest.fixture
def trade_service(stock_service):
    return TradeService(stock_service)
