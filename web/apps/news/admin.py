from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.news.models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('name', 'user', 'created_at',)
    search_fields = ('name', 'description', 'user__username')
    list_filter = ('created_at', 'user')
    raw_id_fields = ('user',)
    readonly_fields = ('created_at',)
