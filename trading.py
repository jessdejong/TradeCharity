import pandas_datareader.data as web
import datetime as dt    
import news_wrapper as nw
import analysis

def backtest(start_year, start_month, start_day, money):
    """Performs a backtest from a certain date, returns article info and start and end price"""

    articles = nw.get_article_info(start_year, start_month, start_day)

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

    #print(articles)
    
    for i in range(len(articles)):
        stockName = articles[i][0]
        sticker = articles[i][1]
        articleName = articles[i][2]
        articleDescription = articles[i][3]
        articleURL = articles[i][4]
        articleDate = articles[i][5]
        date = articleDate.split("-")
        #print(date)

        # sentiment analysis
        sentiment = analysis.analyze(articleDescription)
        
        if (sentiment != 0):
            start = dt.datetime(int(date[0]), int(date[1]), int(date[2][0:date[2].find("T")]))
            end = dt.datetime(int(date[0]), int(date[1]), int(date[2][0:date[2].find("T")]))
            timeSeries = web.DataReader(sticker, 'iex', start, end)
            #print(timeSeries['open'].values[0])

            openVal = timeSeries['open'].values[0]
            closeVal = timeSeries['close'].values[0]

            if (sentiment > 0):
                """ buy the stock """
                if openVal <= money:
                    print("buy")
                    print(closeVal - openVal)
                    print(openVal)
                    print(closeVal)
                    money += (closeVal - openVal) 
            elif (sentiment < 0):
                """ short the stock """
                if openVal <= money:
                    print("short")
                    print(openVal - closeVal)
                    print(openVal)
                    print(closeVal)

                    money += (openVal - closeVal)

            print(articleDescription)
            print(money)

    #aapl = web.DataReader('AAPL', 'iex', start, end)

#def getNextTrade():

backtest(2019, 0, 0, 1000)

#print(aapl.shape)
#print(aapl.head())
