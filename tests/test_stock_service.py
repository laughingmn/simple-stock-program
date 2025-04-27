import pytest


def test_dividend_yield_common(stock_service):
    result = stock_service.dividend_yield("POP", price=120)
    assert round(result, 2) == 0.07


def test_dividend_yield_preferred(stock_service):
    result = stock_service.dividend_yield("GIN", price=100)
    assert round(result, 2) == 0.02


def test_pe_ratio(stock_service):
    result = stock_service.pe_ratio("POP", price=120)
    assert round(result, 2) == 15.0


def test_dividend_yield_invalid_symbol(stock_service):
    with pytest.raises(ValueError, match="Stock INVALID not found"):
        stock_service.dividend_yield("INVALID", price=120)


def test_pe_ratio_invalid_symbol(stock_service):
    with pytest.raises(ValueError, match="Stock INVALID not found"):
        stock_service.pe_ratio("INVALID", price=120)
