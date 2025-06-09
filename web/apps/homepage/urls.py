from django.urls import path

import apps.homepage.views

app_name = "homepage"
urlpatterns = [
    path("", apps.homepage.views.Home.as_view(), name="main"),
]
