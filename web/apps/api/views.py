__all__ = ()

import base64

from rest_framework.authentication import BasicAuthentication
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions, generics
from django.contrib.auth import authenticate
from django.db import models

from apps.news.models import News
from apps.users.models import User, Profile
from apps.classes.models import Class, Computer
from apps.api import serializers
from apps.foods.models import Food, FoodWork
from apps.objects.models import Object, Topic, Subsection


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    http_method_names = ['post']

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                profile = user.profile

                image_data = None
                if profile.image:
                    try:
                        # Получаем оригинальное изображение (не миниатюру)
                        with open(profile.image.path, "rb") as image_file:
                            image_data = base64.b64encode(
                                image_file.read()).decode('utf-8')
                    except Exception as e:
                        print(f"Ошибка обработки изображения: {e}")

                response_data = {
                    "FirstName": user.first_name,
                    "LastName": user.last_name,
                    "Email": user.email,
                    "Login": user.username,
                    "Image": image_data,
                    "Birthday": profile.birthday.strftime("%Y-%m-%d") if profile.birthday else None,
                }

                return Response(response_data)

            except Profile.DoesNotExist:
                return Response(
                    {"error": "Профиль пользователя не найден"},
                    status=status.HTTP_404_NOT_FOUND,
                )
            except Exception as e:
                print(f"Ошибка при получении данных пользователя: {e}")
                return Response(
                    {"error": "Внутренняя ошибка сервера"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        return Response(
            {"error": "Неверные учетные данные"},
            status=status.HTTP_401_UNAUTHORIZED,
        )


class UserListIfMainUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if not User.objects.filter(id=request.user.id, is_superuser=1).exists():
            return Response(
                {"error": "Вы не являетесь главным пользователем"},
                            status=403,
                            )

        users = User.objects
        serializer = serializers.UserSerializer(users, many=True)
        return Response(serializer.data)


class IsOwnerAndTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

    def has_permission(self, request, view):
        return request.user.is_superuser


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ClassSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerAndTeacher]

    def get_queryset(self):
        return Class.objects

    def perform_create(self, serializer):
        serializer.save()


class ComputerViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ComputerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerAndTeacher]

    def get_queryset(self):
        return Computer.objects

    def perform_create(self, serializer):
        serializer.save()


class ComputerByUUIDView(generics.RetrieveAPIView):
    queryset = Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [permissions.AllowAny]  # или настрой свои права
    lookup_field = "uuid"


class UpdateComputerImageView(generics.UpdateAPIView):
    queryset = Computer.objects.all()
    serializer_class = serializers.ComputerSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "uuid"
    http_method_names = ["patch", "put"]


class NewsListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.NewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(
            models.Q(user=user) | models.Q(
                user__id=getattr(user, 'main_user_id', None))
        )

    def perform_create(self, serializer):
        serializer.save()


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.NewsSerializer
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(
            models.Q(user=user) | models.Q(
                user__id=getattr(user, 'main_user_id', None))
        )


class ProblemListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return serializers.Problem.objects

    def perform_create(self, serializer):
        serializer.save()


class ProblemRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = serializers.ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return serializers.Problem.objects


class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = serializers.FoodSerializer
    permission_classes = [permissions.IsAuthenticated]


class FoodWorkViewSet(viewsets.ModelViewSet):
    queryset = FoodWork.objects.all()
    serializer_class = serializers.FoodWorkSerializer
    permission_classes = [permissions.IsAuthenticated]


class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = serializers.ObjectSerializer
    http_method_names = ['get']  # Разрешаем только GET-запросы

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = serializers.TopicSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SubsectionViewSet(viewsets.ModelViewSet):
    queryset = Subsection.objects.all()
    serializer_class = serializers.SubsectionSerializer
    http_method_names = ['get']  # Разрешаем только GET-запросы

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)