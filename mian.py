#pip install requests_html
#pip install yahoo_fin
'''
get_analysts_info()
get_balance_sheet()
get_cash_flow()
get_data()
get_day_gainers()
get_day_losers()
get_day_most_active()
get_holders()
get_income_statement()
get_live_price()
get_quote_table()
get_top_crypto()
get_stats()
get_stats_valuation()
tickers_dow()
tickers_nasdaq()
tickers_other()
tickers_sp500()
'''
from yahoo_fin.stock_info import get_data
import numpy as np
import pandas as pd
from sma30 import sma30 
from macd import macd_
from fibonacci import fibanocii


#get stock data, start date and end date
data= get_data("AAPL", start_date="12/03/2019", end_date="12/10/2021", index_as_date = True, interval="1d")


# get wat type of strategy (sma30 , macd , fibanocci)
x="macd"

if x=="sma30":
    sma30(data)
elif x=="macd":
    macd_(data)
else:
    fibanocii(data)


