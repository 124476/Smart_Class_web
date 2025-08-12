from django.urls import path

from apps.homepage.views import Home, CalendarView, Games, Program

app_name = "homepage"
urlpatterns = [
    path("", Home.as_view(), name="main"),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("games/", Games.as_view(), name="games"),
    path("program/", Program.as_view(), name="program")
]
