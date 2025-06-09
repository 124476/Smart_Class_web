from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.problems.models import Status, Problem


@admin.register(Status)
class StatusAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Problem)
class ProblemAdmin(ModelAdmin):
    list_display = ('name', 'user', 'status', 'created_at',)
    search_fields = ('name', 'description', 'user__username', 'status__name')
    list_filter = ('status', 'created_at', 'user')
    raw_id_fields = ('user', 'status')
    readonly_fields = ('created_at',)