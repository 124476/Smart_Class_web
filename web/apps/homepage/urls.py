from django.urls import path

from apps.homepage.views import Home, CalendarView, Games, Program, AdminProgram

app_name = "homepage"
urlpatterns = [
    path("", Home.as_view(), name="main"),
    path("calendar/", CalendarView.as_view(), name="calendar"),
    path("programs/", Games.as_view(), name="programs"),
    path("school_program/", Program.as_view(), name="school_program"),
    path("admin_program/", AdminProgram.as_view(), name="admin_program"),
]
