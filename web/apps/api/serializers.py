__all__ = ()

import base64

from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from apps.news.models import News
from apps.users.models import User
from apps.classes.models import Class, Computer


class UserSerializer(serializers.ModelSerializer):
    Username = serializers.CharField(source='username')
    FirstName = serializers.CharField(source='first_name')
    LastName = serializers.CharField(source='last_name')
    Email = serializers.EmailField(source='email')
    Avatar = serializers.SerializerMethodField()
    Roles = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'Username',
            'FirstName',
            'LastName',
            'Email',
            'Avatar',
            'Roles',
        ]

    def get_Avatar(self, obj):
        if obj.avatar and hasattr(obj.avatar, 'url'):
            request = self.context.get('request')
            avatar_url = obj.avatar.url
            if request is not None:
                return request.build_absolute_uri(avatar_url)
            return avatar_url
        return None

    def get_Roles(self, obj):
        return list(obj.roles.values_list('name', flat=True))


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = [
            'id',
            'name',
            'user',
        ]


class ComputerSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class_name = serializers.CharField(source='class_obj.name', read_only=True)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = Computer
        fields = [
            'id',
            'name',
            'uuid',
            'is_block',
            'is_sound',
            'is_work',
            'class_obj',
            'class_name',
            'user',
            'image',
            "photo",
            "created_at",
            "updated_at",
        ]

    def get_photo(self, obj):
        if obj.image:
            try:
                file_path = obj.image.path
                with open(file_path, "rb") as image_file:
                    encoded_string = base64.b64encode(
                        image_file.read()).decode('utf-8')
                    return encoded_string
            except Exception as e:
                return None
        return None


class NewsSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    photo = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = [
            'id',
            'name',
            'description',
            'image',
            'user',
            'created_at',
            "photo",
        ]
        read_only_fields = ['user', 'created_at']

    def get_photo(self, obj):
        if obj.image:
            try:
                file_path = obj.image.path
                with open(file_path, "rb") as image_file:
                    encoded_string = base64.b64encode(
                        image_file.read()).decode('utf-8')
                    return encoded_string
            except Exception as e:
                return None
        return None
