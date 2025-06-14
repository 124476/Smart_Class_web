from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.objects.models import Object, Topic, Subsection


@admin.register(Object)
class ObjectAdmin(ModelAdmin):
    list_display = ('id', 'name', 'user')
    search_fields = ('name', 'user__username')
    list_filter = ('user',)
    raw_id_fields = ('user',)


@admin.register(Topic)
class TopicAdmin(ModelAdmin):
    list_display = ('id', 'name', 'object')
    search_fields = ('name', 'object__name')
    list_filter = ('object',)
    raw_id_fields = ('object',)


@admin.register(Subsection)
class SubsectionAdmin(ModelAdmin):
    list_display = ('id', 'name', 'topic')
    search_fields = ('name', 'description', 'topic__name')
    list_filter = ('topic',)
    raw_id_fields = ('topic',)