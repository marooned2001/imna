from django.shortcuts import render
from django.http import HttpResponse
from .models import News


def home(request):
    news_list = list(News.objects.all())
    first_news = news_list[0]
    return render(request, 'home.html', {'news_list': news_list, 'first_news': first_news})


def news(request, news_id):
    news_list = list(News.objects.all())
    new = News.objects.get(pk=news_id)
    return render(request, 'news.html', {'new': new, 'news_list': news_list})


def contact_us(request):
    return render(request, 'contact.html')


def about_us(request):
    return render(request, 'about.html')
