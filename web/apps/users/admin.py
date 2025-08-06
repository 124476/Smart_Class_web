from unfold.admin import ModelAdmin

import django.contrib
import django.contrib.auth.admin
import django.contrib.auth.models

from apps import users


class ProfileInline(django.contrib.admin.TabularInline):
    model = users.models.Profile
    fk_name = 'user'
    can_delete = False
    readonly_fields = [
        users.models.Profile.birthday.field.name,
        users.models.Profile.image.field.name,
    ]


@django.contrib.admin.register(users.models.User)
class UserAdmin(ModelAdmin):
    inlines = (ProfileInline,)


django.contrib.admin.site.unregister(
    users.models.User,
)

django.contrib.admin.site.register(users.models.User, UserAdmin)

__all__ = ()
