from newsapi import NewsApiClient
import requests
import json

# URL as well as json data


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
compani_file = open("compani.txt", "r")
companies = compani_file.readlines()
def get_article_info(year, month, day):
    url = ('https://newsapi.org/v2/everything?'
    'q=Apple&'
    'from={year}-{month}-{day}&'
    'sortBy=popularity&'
    'apiKey=4383f2a732424f11b00dbb7b3e3bce64')
    response = requests.get(url)
    data = response.json()

    array = []
    for i in range(len(data['articles'])):
        print(data['articles'][i])
        for j in companies:
            j = j.rstrip('\n')
            symbol = j[j.rfind(" ")+1:len(j)]
            j = j[0:j.rfind(" ")]
            if j.lower() in data['articles'][i]['title'].lower() or j.lower() in data['articles'][i]['description'].lower():
                print(data['articles'][i]['title'])
                array.append([j, symbol, data['articles'][i]['title'], data['articles'][i]['description'], data['articles'][i]['url'], data['articles'][i]['publishedAt']])
    return array