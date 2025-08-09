from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.classes.models import Class, Computer


@admin.register(Class)
class ClassAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Computer)
class ComputerAdmin(ModelAdmin):
    list_display = ('id', 'name', 'is_block', 'is_sound', 'is_work', 'class_obj',)
    list_filter = ('is_block', 'is_sound', 'is_work', 'class_obj',)
    search_fields = ('name', 'class_obj__name',)
    raw_id_fields = ('class_obj',)
    readonly_fields = ()
