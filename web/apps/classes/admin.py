from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.classes.models import Class, Computer


@admin.register(Class)
class ClassAdmin(ModelAdmin):
    list_display = ('name', 'user',)
    search_fields = ('name', 'user__username', 'user__email')
    list_filter = ('user',)


@admin.register(Computer)
class ComputerAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_block', 'is_sound', 'is_work', 'class_obj', 'user')
    list_filter = ('is_block', 'is_sound', 'is_work', 'class_obj', 'user')
    search_fields = ('name', 'class_obj__name', 'user__username')
    raw_id_fields = ('class_obj', 'user')
    readonly_fields = ()
