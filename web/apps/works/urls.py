from django.urls import path
from apps.works import views

app_name = "works"

urlpatterns = [
    path("", views.DashboardView.as_view(), name="dashboard"),
    path("events/", views.EventListView.as_view(), name="events"),
    path("events/add/", views.EventCreateView.as_view(), name="event_add"),
    path("events/<int:pk>/edit/", views.EventUpdateView.as_view(), name="event_edit"),
    path(
        "events/<int:pk>/delete/", views.EventDeleteView.as_view(), name="event_delete"
    ),
    path("feedback/", views.FeedbackView.as_view(), name="feedback"),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
]
