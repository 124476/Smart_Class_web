from django.views.generic import ListView, DetailView
from apps.news.models import News


class Description(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail_news.html'
    context_object_name = 'news'
