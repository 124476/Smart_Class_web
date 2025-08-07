from django.urls import path

from apps.news.views import NewsDetailView, Description


app_name = "news"
urlpatterns = [
    path("news/", Description.as_view(), name="main"),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
]
