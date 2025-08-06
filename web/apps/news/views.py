from django.views.generic import ListView
from apps.news.models import News


class Description(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"
