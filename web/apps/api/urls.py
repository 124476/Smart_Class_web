from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.api import views

app_name = "api"

router = DefaultRouter()
router.register(r'classes', views.ClassViewSet, basename='class')
router.register(r'computers', views.ComputerViewSet, basename='computer')
router.register(r'foods', views.FoodViewSet)
router.register(r'foodworks', views.FoodWorkViewSet)
router.register('objects', views.ObjectViewSet)
router.register('topics', views.TopicViewSet)
router.register('subsections', views.SubsectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('users/', views.UserListIfMainUserAPIView.as_view(), name='user-list-if-main'),
    path("computers_connection/<uuid:uuid>/", views.ComputerByUUIDView.as_view(), name="computer-by-uuid"),
    path("computers_connection/<uuid:uuid>/update-image/", views.UpdateComputerImageView.as_view(), name="update-computer-image"),
    path('news/', views.NewsListCreateView.as_view(), name='news-list-create'),
    path('news/<int:id>/', views.NewsRetrieveUpdateDestroyView.as_view(), name='news-detail'),
    path("problems/", views.ProblemListCreateView.as_view(), name="problem-list-create"),
    path("problems/<int:id>/", views.ProblemRetrieveUpdateView.as_view(), name="problem-detail"),
]
