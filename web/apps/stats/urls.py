import django.urls

import apps.stats.views

app_name = "stats"
urlpatterns = [
    django.urls.path("", apps.stats.views.AnalyticsView.as_view(), name="stats"),
]
