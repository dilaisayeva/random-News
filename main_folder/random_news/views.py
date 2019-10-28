from django.shortcuts import render
import requests
# Create your views here.

def random_news(request):
    context = {}
    url_news_api = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=21b212c0ebf94bff9654985e42988436'
    response = requests.get(url_news_api)
    res_json = response.json()
    articles = res_json['articles']
    context['articles'] = articles

    return render(request,'random_news.html',context)