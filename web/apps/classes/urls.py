import django.urls
import django.views.generic

import apps.classes.views


app_name = "classes"
urlpatterns = [
    django.urls.path("", apps.classes.views.Description.as_view(), name="main"),
]
