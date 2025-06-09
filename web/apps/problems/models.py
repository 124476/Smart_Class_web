from django.db import models
from django.conf import settings


class Status(models.Model):
    name = models.CharField(
        verbose_name="Название статуса",
        max_length=100,
    )

    def __str__(self):
        return self.name


class Problem(models.Model):
    name = models.CharField(
        verbose_name="Название проблемы",
        max_length=200,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="problems",
        verbose_name="Пользователь",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="problems",
        verbose_name="Статус",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
    )

    created_at = models.DateTimeField(
        verbose_name="Создано",
        auto_now_add=True,
    )

    def __str__(self):
        return f"{self.name} — {self.status.name if self.status else 'Без статуса'}"
