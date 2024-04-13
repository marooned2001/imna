from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'home.html')

def contact_us(request):
    return render(request, 'home.html')

def about_us(request):
    return render(request, 'home.html')

