# Notes from tha boss Mr Sentdex himself:

# pandas = excel spreadsheets
# python is faster than excel
#
# python is theoritically slower than c
#     in reality it is just as fast
#     and the syntax is easy
#
# pandas makes life easy


import pandas as pd
import datetime
import pandas_datareader.data as web


# HUGE!!!: import pandas_datareader.data as web
#     Was getting the ERR: ImportError: cannot import name 'is_list_like'
#
#     So I updated to the latest development version of pandas_datareader: pip install git+https://github.com/pydata/pandas-datareader.git


import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')     # or 'fivethirtyeight'

start = datetime.datetime(1997,11,28)
end = datetime.datetime.now()


# HUGE NOTE!!!:
# Morningstar has been immediately deprecated due to large breaks in the API without the
# introduction of a stable replacement. Pull Requests to re-enable these data
# connectors are welcome.
#
# So sentdex's line: df = web.DataReader("XOM", "morningstar", start, end)
# Has to be replaced with: df = web.get_data_yahoo('AAPL', start=start, end=end)
# As seen below

print('Downloading data...')
df = web.get_data_yahoo('GOOG', start=start, end=end)
print('Download complete...')

print(df.head())

df['Adj Close'].plot()

plt.show()
