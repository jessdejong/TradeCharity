import pandas_datareader.data as web
import datetime as dt    
import news_wrapper as nw

def backtest(start_year, start_month, start_day, money):
    """Performs a backtest from a certain date, returns article info and start and end price"""
    start = dt.datetime(start_year, start_month, start_day)
    end = dt.datetime.now()

    #articles = get_article_info(start_year, start_month, start_day)
    articles = nw.get_article_info()

    """
    For each article, check whether the sentiment is positive or negative.
    If positive:
        buy that stock (at that certain day) if we have enough money - at open?
        sell at close
        update our money
    If negative:
        short sell that stock at open if we have enough money - at open
        update money
    """

    print(articles)
    
    for i in range(len(articles)):
        print(i)
    
    

    #aapl = web.DataReader('AAPL', 'iex', start, end)

#def getNextTrade():
    


backtest(2018, 10, 1, 1000)



#print(aapl.shape)
#print(aapl.head())
