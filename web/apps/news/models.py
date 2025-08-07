from django.db import models
from django.conf import settings
from django.urls import reverse


class News(models.Model):
    name = models.CharField(
        verbose_name="Заголовок",
        max_length=200,
    )
    description = models.TextField(
        verbose_name="Описание",
    )
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="news/",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="news",
        verbose_name="Автор",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания",
        auto_now_add=True,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('news:news_detail', kwargs={'pk': self.pk})
