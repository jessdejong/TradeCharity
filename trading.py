'''import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
df = web.DataReader("TSLA", 'iex', start, end)
df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
df = df.drop("Symbol", axis=1)

print(df.head())
'''

import pandas_datareader.data as web
import datetime as dt    

def backtest(start_year, start_month, start_day):

    start = dt.datetime(start_year, start_month, start_day)
    end = dt.datetime.now()

    aapl = web.DataReader('AAPL', 'iex', start, end)

def getNextTrade():
    


backtest(2018, 10, 1)



print(aapl.shape)
print(aapl.head())
