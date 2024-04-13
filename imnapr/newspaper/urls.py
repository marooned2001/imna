from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('news/<int:id>, views.news')
]




