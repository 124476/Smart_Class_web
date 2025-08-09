from django.db import models
from django.conf import settings


class Food(models.Model):
    name = models.CharField(
        verbose_name="Название блюда",
        max_length=100,
    )
    price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
    )

    def __str__(self):
        return f"{self.name} ({self.price}₽)"


class FoodWork(models.Model):
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        related_name="usages",
        verbose_name="Блюдо",
    )
    date = models.DateField("Дата")

    def __str__(self):
        return f"{self.food.name} - {self.date}"
