from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.works.models import Event, Feedback


@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = (
        "title",
        "date",
    )


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    list_display = (
        "user",
        "message",
    )
