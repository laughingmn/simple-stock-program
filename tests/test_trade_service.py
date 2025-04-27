import pytest

from src.models.stock import CommonStock
from src.services.stock_service import StockService
from src.services.trade_service import TradeService
from src.utils.trade_indicator import TradeIndicator


@pytest.fixture
def stock_service():
    service = StockService()
    service.add_stock(CommonStock(symbol="TEA", last_dividend=0, par_value=100))
    service.add_stock(CommonStock(symbol="POP", last_dividend=8, par_value=100))
    return service


@pytest.fixture
def trade_service(stock_service):
    return TradeService(stock_service)


def test_record_trade_success(trade_service):
    trade_service.record_trade(symbol="TEA", quantity=50, indicator=TradeIndicator.BUY, price=110)
    trades = trade_service.get_trades_in_last_minutes("TEA")
    assert len(trades) == 1
    assert trades[0].symbol == "TEA"
    assert trades[0].price == 110


def test_record_trade_invalid_symbol(trade_service):
    with pytest.raises(ValueError, match="Stock INVALID not found"):
        trade_service.record_trade(symbol="INVALID", quantity=10, indicator=TradeIndicator.BUY, price=100)


def test_record_trade_quantity(trade_service):
    trade_service.record_trade(symbol="POP", quantity=15, indicator=TradeIndicator.BUY, price=100)
    trades = trade_service.get_trades_in_last_minutes("POP")
    assert trades[0].quantity == 15


def test_get_trades_in_last_minutes(trade_service):
    trade_service.record_trade(symbol="POP", quantity=10, indicator=TradeIndicator.SELL, price=150)
    trade_service.record_trade(symbol="POP", quantity=20, indicator=TradeIndicator.SELL, price=155)

    trades = trade_service.get_trades_in_last_minutes("POP", minutes=15)
    assert len(trades) == 2


def test_volume_weighted_stock_price(trade_service):
    trade_service.record_trade(symbol="POP", quantity=10, indicator=TradeIndicator.BUY, price=120)
    trade_service.record_trade(symbol="POP", quantity=20, indicator=TradeIndicator.SELL, price=130)
    vwsp = trade_service.volume_weighted_stock_price("POP")
    assert round(vwsp, 2) == 126.67


def test_volume_weighted_stock_price_no_trades(trade_service):
    vwsp = trade_service.volume_weighted_stock_price("TEA")
    assert vwsp == 0.0


def test_geometric_mean(trade_service):
    trade_service.record_trade(symbol="TEA", quantity=10, indicator=TradeIndicator.BUY, price=100)
    trade_service.record_trade(symbol="POP", quantity=20, indicator=TradeIndicator.SELL, price=200)
    gm = trade_service.geometric_mean()
    assert round(gm, 2) == 141.42
