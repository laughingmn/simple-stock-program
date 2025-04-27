from src.models.stock import CommonStock, NotPrefereed, PreferredStock

STOCKS = [
    CommonStock(symbol="TEA", last_dividend=0, par_value=100),
    CommonStock(symbol="POP", last_dividend=8, par_value=100),
    CommonStock(symbol="ALE", last_dividend=23, par_value=60),
    PreferredStock(symbol="GIN", last_dividend=8, fixed_dividend=0.02, par_value=100),
    NotPrefereed(symbol="JIN", last_dividend=23, par_value=60),
    CommonStock(symbol="JOE", last_dividend=13, par_value=250),
]
