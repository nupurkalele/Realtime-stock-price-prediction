pip install newsapi-python
!pip install yfinance
!pip install requests
!pip install transformers
import datetime, requests, yfinance
from newsapi import NewsApiClient
from getpass import getpass

#initialising
newsapi = NewsApiClient(api_key='a6e2f4eb2869408ebeb2c5df7a2d9764')


#to obtain news headlines
top_headlines = newsapi.get_top_headlines(q='stocks',
                                          qintitle='Netflix',
                                          category='business',
                                          language='en',
                                          country='in')


#top_headlines

# /v2/everything
all_articles = newsapi.get_everything(q='stocks',
                                      qintitle='netflix',
                                      domains='bbc.co.uk,techcrunch.com',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
all_articles



# /v2/top-headlines/sources
sources = newsapi.get_sources()
#sources
# Accessing the articles
articles = top_headlines['articles']
#articles

#to fetch earnings

ticker=yfinance.Ticker("NFLX")
ES= ticker.get_earnings_dates()
ES.head()

#ticker.news
from transformers import pipeline
classifier= pipeline('sentiment-analysis')
#example for sentiment scores
classifier('the fox crossed the road and got hit by a car and was injured')
# Extracting titles for classification
titles_for_classification = [article['title'] for article in articles]
titles_for_classification

#classifier is a function that takes text for classification
classifier_result = classifier(titles_for_classification)

#Printing the classification result
classifier_result

