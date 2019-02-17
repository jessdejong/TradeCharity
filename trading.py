import pandas_datareader.data as web
import datetime as dt    
import news_wrapper as nw
import analysis

def backtest(start_year, start_month, start_day, money):
    """Performs a backtest from a certain date, returns article info and start and end price"""

    output = ""

    start_year = int(start_year)
    start_month = int(start_month)
    start_day = int(start_day)
    money = float(money)

    articles = nw.get_article_info(start_year, start_month, start_day)
    # print(articles)
    
    for i in range(len(articles)):
        stockName = articles[i][0]
        sticker = articles[i][1]
        articleName = articles[i][2]
        articleDescription = articles[i][3]
        articleURL = articles[i][4]
        articleDate = articles[i][5]
        date = articleDate.split("-")

        # sentiment analysis
        sentiment = analysis.analyze(articleDescription)
        
        if (sentiment != 0):
            start = dt.datetime(int(date[0]), int(date[1]), int(date[2][0:date[2].find("T")]))
            end = dt.datetime(int(date[0]), int(date[1]), int(date[2][0:date[2].find("T")]))
            timeSeries = web.DataReader(sticker, 'iex', start, end)

            try:
                openVal = timeSeries['open'].values[0].astype(int).item()
                closeVal = timeSeries['close'].values[0].astype(int).item()
            except:
                continue

            #print(sticker)
            #print(articleName) 
            #print(money)

            #print (sentiment)
            if (sentiment > 0):
                """ buy the stock """
                if openVal <= money:
                    numStocks = int(money/2/openVal)
                    if numStocks < 1:
                        numStocks = 1
                    #print("buy")
                    #print(numStocks)
                    #print(closeVal - openVal)
                    #print(openVal)
                    #print(closeVal)
                    money += numStocks * (closeVal - openVal) 
            elif (sentiment < 0):
                """ short the stock """
                if openVal <= money:
                    numStocks = int(money/2/openVal)
                    if numStocks < 1:
                        numStocks = 1
                    #print("short")
                    #print(numStocks)
                    #print(openVal - closeVal)
                    #print(openVal)
                    #print(closeVal)

                    money += numStocks * (openVal - closeVal)
            
            array = [stockName, sticker, articleName, articleDescription, articleURL, articleDate, sentiment, money, numStocks, openVal, closeVal, date[0], date[1], date[2][0:date[2].find("T")]]
            #stockName|sticker|articleName|articleDescription|articleURL|articleDate|sentiment|money|numStocks|openVal|closeVal|year|month|day\n
            output += '|'.join(map(str, array)) + "\n"
            
    return str(output)

# backtest(2019, 0, 0, 1000)
