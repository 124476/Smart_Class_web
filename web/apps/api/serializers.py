__all__ = ()

import base64

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from drf_extra_fields.fields import Base64ImageField

from apps.news.models import News
from apps.users.models import User
from apps.classes.models import Class, Computer
from apps.problems.models import Problem, Status
from apps.foods.models import Food, FoodWork
from apps.objects.models import Object, Topic, Subsection


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
                        image_file.read(),
                    ).decode('utf-8')
                    return encoded_string
            except Exception as e:
                return None
        return None


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'name']


class ProblemSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(source='status.name', read_only=True)

    class Meta:
        model = Problem
        fields = [
            'id',
            'name',
            'description',
            'status',
            'status_name',
            'user',
            'created_at',
        ]
        read_only_fields = ['user', 'created_at']


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'price', 'user']


class FoodWorkSerializer(serializers.ModelSerializer):
    food_name = serializers.ReadOnlyField(source='food.name')

    class Meta:
        model = FoodWork
        fields = ['id', 'food', 'food_name', 'date']

    def validate(self, data):
        food = data.get('food')
        date = data.get('date')

        if FoodWork.objects.filter(food=food, date=date).exclude(id=self.instance.id if self.instance else None).exists():
            raise ValidationError("Запись с таким food и date уже существует.")
        return data


class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ['id', 'name', 'user']


class TopicSerializer(serializers.ModelSerializer):
    object_name = serializers.CharField(source='object.name', read_only=True)

    class Meta:
        model = Topic
        fields = ['id', 'name', 'object', 'object_name']


class SubsectionSerializer(serializers.ModelSerializer):
    topic_name = serializers.CharField(source='topic.name', read_only=True)

    class Meta:
        model = Subsection
        fields = ['id', 'name', 'description', 'topic', 'topic_name']