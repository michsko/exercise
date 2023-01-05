import requests
import datetime


def get_news(name):
    news_api = "ea795d98b45e48ababf06cd2ae0d734e"
    searched_name = name
    news_parameters = news_parameters = {"q": searched_name,
                                         "sortBy": "publishedAT",
                                         "apiKey": news_api}

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()
    print(news)

    in_title = news


