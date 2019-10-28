from django.contrib import admin
from django.urls import path,include
from random_news.views import random_news

urlpatterns = [
    path('', random_news, name='news')
]