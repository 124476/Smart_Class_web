from django.urls import path
from apps.users import views

app_name = "users"

urlpatterns = [
    path("signup/", views.RegisterView.as_view(), name="register"),
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path('delete_avatar/', views.delete_avatar, name='delete_avatar'),
]
