from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание", blank=True)
    date = models.DateField("Дата проведения")
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ["-date"]
        verbose_name = "Событие"
        verbose_name_plural = "События"

    def __str__(self):
        return f"{self.title} — {self.date}"

    def get_absolute_url(self):
        return reverse('works:event_detail', kwargs={'pk': self.pk})


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата отправки", auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"Отзыв от {self.user} — {self.created_at.strftime('%Y-%m-%d %H:%M')}"
