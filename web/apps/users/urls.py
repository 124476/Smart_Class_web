from django.urls import path
from apps.users.views import (
    RegisterView,
    CustomLoginView,
    CustomLogoutView,
    AccountView,
    PasswordChangeView,
    PasswordChangeDoneView
)

app_name = "users"

urlpatterns = [
    path(
        'signup/',
        RegisterView.as_view(),
        name='signup',
    ),
    path(
        'login/',
        CustomLoginView.as_view(),
        name='login',
    ),
    path(
        'logout/', CustomLogoutView.as_view(),
        name='logout',
    ),
    path(
        'profile/', AccountView.as_view(),
        name='profile',
    ),
    path(
        'password-change/',
        PasswordChangeView.as_view(),
        name='password_change',
    ),
    path(
        'password-change/done/',
        PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),
]
