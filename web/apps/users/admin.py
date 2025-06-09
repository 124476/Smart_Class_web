from unfold.admin import ModelAdmin

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from apps.users.models import User, Role

admin.site.unregister(Group)


@admin.register(Role)
class RoleAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_created', 'main_user')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'is_created', 'roles')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Личные данные', {'fields': ('first_name', 'last_name', 'email', 'avatar', 'roles', 'main_user', 'is_created')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )

    filter_horizontal = ('roles', 'groups', 'user_permissions')