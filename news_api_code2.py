import requests

def sports_news():
    api_key = "e44acfad9a8d4734b43fa5b79f882c21"
    url = "https://newsapi.org/v2/top-headlines?country=ng&category=sports&apiKey="+api_key
    news = requests.get(url).json()
    
    article = news["articles"]

    news_article = []
    for arti in article:
        news_article.append(arti["title"])
    
    for index, value in enumerate(news_article) :
        print(index+1, value)


# def politics_news():
#     url = "https://newsapi.org/v2/top-headlines?country=ng&category=politics&apiKey="+api_key
#     news = requests.get(url).json()
    
#     article = news["articles"]
    

#     news_article = []
#     for arti in article:
#         news_article.append(arti["title"])
    

#     for i in range(10):
#         print(i+1, news_article[i])


# def music_news():
#     url = "https://newsapi.org/v2/top-headlines?country=ng&category=music&apiKey="+api_key
#     news = requests.get(url).json()
    
#     article = news["articles"]
    

#     news_article = []
#     for arti in article:
#         news_article.append(arti["title"])
    

#     for i in range(10):
#         print(i+1, news_article[i])
       



sports_news()




