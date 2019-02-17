from newsapi import NewsApiClient
import requests
import json

# URL as well as json data
url = ('https://newsapi.org/v2/everything?'
    'q=Apple&'
    'from=2019-02-16&'
    'sortBy=popularity&'
    'apiKey=4383f2a732424f11b00dbb7b3e3bce64')
response = requests.get(url)
data = response.json()

# Init
newsapi = NewsApiClient(api_key='4383f2a732424f11b00dbb7b3e3bce64')

# # /v2/everything
# all_articles = newsapi.get_everything(q='bitcoin',
#                                       sources='bbc-news,the-verge',
#                                       domains='bbc.co.uk,techcrunch.com',
#                                       from_param='2017-12-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)

# /v2/sources
sources = newsapi.get_sources()

def headlines():
    array = []
    for i in data['articles']:
        array.append(i['title'])
    return array

def descriptions():
    array = []
    for i in data['articles']:
        array.append(i['description'])
    return array
