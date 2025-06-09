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
from apps.users.models import User
from apps.classes.models import Class, Computer
from apps.api.serializers import UserSerializer, ClassSerializer, \
    ComputerSerializer, NewsSerializer


class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login = user.username

            image_base64 = None
            if user.avatar and user.avatar.path:
                try:
                    with open(user.avatar.path, "rb") as image_file:
                        encoded_string = base64.b64encode(
                            image_file.read()).decode('utf-8')
                        image_base64 = encoded_string
                except Exception as e:
                    print(e)
                    image_base64 = None

            roles = list(user.roles.values_list('name', flat=True))

            return Response({
                "FirstName": user.first_name,
                "LastName": user.last_name,
                "Email": user.email,
                "Login": login,
                "Image": image_base64,
                "MainUser": user.main_user_id,
                "Roles": roles,
            })
        return Response({"error": "Неверные учетные данные"},
                        status=status.HTTP_401_UNAUTHORIZED)


class UserListIfMainUserAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        if not User.objects.filter(id=request.user.id, is_created=1).exists():
            return Response({"error": "Вы не являетесь главным пользователем"},
                            status=403)

        users = User.objects.filter(main_user_id=request.user.id, is_created=0)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class IsOwnerAndTeacher(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_owner = obj.user == request.user

        roles = request.user.roles.values_list('name', flat=True)
        is_teacher = "Учитель" in roles

        return is_owner and is_teacher

    def has_permission(self, request, view):
        roles = request.user.roles.values_list('name', flat=True)
        return "Учитель" in roles


class ClassViewSet(viewsets.ModelViewSet):
    serializer_class = ClassSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerAndTeacher]

    def get_queryset(self):
        return Class.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ComputerViewSet(viewsets.ModelViewSet):
    serializer_class = ComputerSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerAndTeacher]

    def get_queryset(self):
        return Computer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ComputerByUUIDView(generics.RetrieveAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [permissions.AllowAny]  # или настрой свои права
    lookup_field = "uuid"


class UpdateComputerImageView(generics.UpdateAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "uuid"
    http_method_names = ["patch", "put"]


class NewsListCreateView(generics.ListCreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(
            models.Q(user=user) | models.Q(
                user__id=getattr(user, 'main_user_id', None))
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NewsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(
            models.Q(user=user) | models.Q(
                user__id=getattr(user, 'main_user_id', None))
        )
