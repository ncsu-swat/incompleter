#Source: https://stackoverflow.com/questions/76187352/how-to-resolve-attributeerror-in-yfinance-library-while-getting-historical-s
import yfinance as yf
import pandas as pd

# Get data for TSLA
tsla = yf.Ticker("TSLA")

# Get historical stock data for TSLA
stock_data = tsla.history(period="max")

# Remove any timezone information from the index
stock_data.index = stock_data.index.tz_localize(None)

# Convert the index to a pandas DatetimeIndex in UTC timezone
stock_data.index = pd.DatetimeIndex(stock_data.index, tz="UTC")