from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('api/news', views.NewsList.as_view()),
    path('api/news/<id>', views.NewsDescription.as_view())
]
