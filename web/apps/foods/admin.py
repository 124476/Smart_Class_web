from unfold.admin import ModelAdmin

from django.contrib import admin

from apps.foods.models import Food, FoodWork


@admin.register(Food)
class FoodAdmin(ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)
    list_filter = ('price',)


@admin.register(FoodWork)
class FoodWorkAdmin(ModelAdmin):
    list_display = ('id', 'food', 'date')
    search_fields = ('food__name',)
    list_filter = ('date',)
    raw_id_fields = ('food',)