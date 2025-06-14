import os
import uuid

from django.db import models
from django.conf import settings


class Class(models.Model):
    name = models.CharField(
        verbose_name="Название класса",
        max_length=100,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="classes",
        verbose_name="Пользователь",
    )

    def __str__(self):
        return self.name


class Computer(models.Model):
    uuid = models.UUIDField(
        verbose_name="Уникальный идентификатор",
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    name = models.CharField(
        verbose_name="Название компьютера",
        max_length=100,
    )
    is_block = models.BooleanField(
        verbose_name="Заблокирован",
        default=False,
    )
    is_sound = models.BooleanField(
        verbose_name="Звук включен", default=True,
    )
    is_work = models.BooleanField(
        verbose_name="Работает",
        default=True,
    )
    class_obj = models.ForeignKey(
        Class,
        on_delete=models.CASCADE,
        related_name="computers",
        verbose_name="Класс",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="computers",
        verbose_name="Пользователь",
    )
    image = models.ImageField(
        "Изображение",
        upload_to="computers/",
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата обновления",
        auto_now=True,
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        try:
            old = Computer.objects.get(pk=self.pk)
        except Computer.DoesNotExist:
            old = None

        super().save(*args, **kwargs)  # сначала сохраняем новый объект (чтобы был id)

        if old and old.image and self.image and old.image != self.image:
            old_image_path = old.image.path
            if os.path.isfile(old_image_path):
                os.remove(old_image_path)