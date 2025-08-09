from django.urls import path

from apps.problems import views

app_name = "problems"

urlpatterns = [
    path("problems/", views.ProblemListView.as_view(), name="problems"),
    path("problems/add/", views.ProblemCreateView.as_view(), name="problem_add"),
    path("problems/<int:pk>/edit/", views.ProblemUpdateView.as_view(), name="problem_edit"),
    path(
        "problems/<int:pk>/delete/", views.ProblemDeleteView.as_view(), name="problem_delete"
    ),
    path('problems/<int:pk>/', views.ProblemDetailView.as_view(), name='problem_detail'),
]
