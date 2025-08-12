from django.urls import path

from apps.works.views import DashboardView, EventListView, EventCreateView, \
    EventUpdateView, EventDeleteView, EventDetailView, AdminProgramView

app_name = "works"

urlpatterns = [
    path("", DashboardView.as_view(), name="dashboard"),
    path("events/", EventListView.as_view(), name="events"),
    path("events/add/", EventCreateView.as_view(), name="event_add"),
    path("events/<int:pk>/edit/", EventUpdateView.as_view(),
         name="event_edit"),
    path(
        "events/<int:pk>/delete/", EventDeleteView.as_view(),
        name="event_delete",
    ),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('events/admin_program/', AdminProgramView.as_view(),
         name='admin_program'),
]
