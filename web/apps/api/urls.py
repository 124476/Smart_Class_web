from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.api import views

app_name = "api"

router = DefaultRouter()
router.register(r'classes', views.ClassViewSet, basename='class')
router.register(r'computers', views.ComputerViewSet, basename='computer')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('users/', views.UserListIfMainUserAPIView.as_view(), name='user-list-if-main'),
    path("computers_connection/<uuid:uuid>/", views.ComputerByUUIDView.as_view(), name="computer-by-uuid"),
    path("computers_connection/<uuid:uuid>/update-image/", views.UpdateComputerImageView.as_view(), name="update-computer-image"),
    path('news/', views.NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:id>/', views.NewsRetrieveUpdateDestroyView.as_view(), name='news-detail'),
]
