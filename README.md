# TradeCharity
Our goal is to help address the homelessness issue in Dallas, by trading stocks via sentiment analysis.

# Inspiration
As residents of Dallas, we have first hand experience with the pros and cons of our city. Our experiences walking through the streets of Dallas and Richardson have inspired us to make an application that focuses on solving homelessness.

Dallas has an extremely high rate of homelessness. As citizens of the Dallas community, we have been instilled with a desire to make our city the best in Texas and even the United States. But this is not a problem. This is actually an opportunity. This is our chance to help our fellow Texans as well as Dallas. Trade Charity is here to jump on this chance and help our city.

# What it does
Trade Charity is an innovative app that reads from news articles for company names that we have whitelisted. Once we have found an article, we use IBM Watson to automate the calculation of the sentiment, telling us if the article was "good" or "bad" for the selected company.

This sentiment is analyzed by our stock trading algorithm. Depending on the sentiment, it may run the decision of buy/selling a stock.

After a few weeks or months of profit, we allow the user to select from a list of local homelessness shelters as well as select local charities to donate their earnings to. We give the user a sense of belonging in the Dallas community, as well as the knowledge that they have helped their community.

# How we built it
We used several APIs to help us reach our goal. We used an API to get the news, where we checked if it had a company name we had white-listed. There we would get the sentiment of the headline and description and see if the company was associated with a positive or negative connotation. Depending on the connotation, our bot may either buy, hold, or sell a share.

# Accomplishments that we're proud of
Getting our various APIs to run without any significant problems.

# What's next for Trade Charity
Optimize the gains of the buy/hold/sell algorithm. Implement our algorithm with real money.

# Set Up
clone repo

`pip install flask`

`pip install newsapi-python`

`pip install watson_developer_cloud`

`pip install pandas_datareader`

`pip install pymapd`

`export FLASK_APP=app.py`

`flask run`

# Contributors
Syed Abutalib, Jess DeJong, Syed Pervaiz
