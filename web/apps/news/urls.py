import django.urls
import django.views.generic

import apps.news.views


app_name = "news"
urlpatterns = [
    django.urls.path("", apps.news.views.Description.as_view(), name="main"),
]
