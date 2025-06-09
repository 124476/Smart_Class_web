import django.urls
import django.views.generic

import apps.about.views


app_name = "about"
urlpatterns = [
    django.urls.path("", apps.about.views.Description.as_view(), name="main"),
]
