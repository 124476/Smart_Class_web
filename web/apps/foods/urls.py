import django.urls
import django.views.generic

import apps.foods.views


app_name = "foods"
urlpatterns = [
    django.urls.path("", apps.foods.views.Description.as_view(), name="main"),
]
