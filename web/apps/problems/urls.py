import django.urls
import django.views.generic

import apps.problems.views


app_name = "problems"
urlpatterns = [
    django.urls.path("", apps.problems.views.Description.as_view(), name="main"),
]
