from src.data.sample_data import STOCKS
from src.services.stock_service import StockService
from src.services.trade_service import TradeService
from src.utils.logger import logger
from src.utils.trade_indicator import TradeIndicator


def main():
    """
    - Adds stocks
    - Records trades
    - Calculates financial metrics like Dividend Yield, P/E Ratio, VWSP, and GBCE All Share Index
    """

    stock_service = StockService()
    trade_service = TradeService(stock_service)

    try:
        # Add Stocks
        for stock in STOCKS:
            stock_service.add_stock(stock)

        # Record Trades
        trade_service.record_trade(symbol="TEA", quantity=100, indicator=TradeIndicator.BUY, price=110)
        trade_service.record_trade(symbol="POP", quantity=50, indicator=TradeIndicator.SELL, price=151)
        trade_service.record_trade(symbol="TEA", quantity=200, indicator=TradeIndicator.BUY, price=111)
        trade_service.record_trade(symbol="ALE", quantity=30, indicator=TradeIndicator.BUY, price=62)
        trade_service.record_trade(symbol="JIN", quantity=30, indicator=TradeIndicator.BUY, price=62)

        # Dividend Yield
        dividend_yield_pop = stock_service.dividend_yield("POP", 120)
        print(f"Dividend Yield for 'POP': {round(dividend_yield_pop, 2)}")
        dividend_yield_pop = stock_service.dividend_yield("GIN", 100)
        print(f"Dividend Yield for 'POP': {round(dividend_yield_pop, 2)}")
        # PE Ratio
        pe_ratio_pop = stock_service.pe_ratio("POP", 120)
        print(f"P/E Ratio for 'POP': {round(pe_ratio_pop, 2)}")

        # VWSP
        vwsp_pop = trade_service.volume_weighted_stock_price("POP")
        print(f"Volume Weighted Stock Price (VWSP) for 'POP': {round(vwsp_pop, 2)}")
        vwsp_ale = trade_service.volume_weighted_stock_price("ALE")
        print(f"Volume Weighted Stock Price (VWSP) for 'ALE': {round(vwsp_ale, 2)}")

        # Geometric Mean
        geometric_mean = trade_service.geometric_mean()
        print(f"Geometric Mean of all trade prices: {round(geometric_mean, 2)}")

    except ValueError as e:
        logger.error(f"An error occurred during operation: {e}")


if __name__ == "__main__":
    main()
