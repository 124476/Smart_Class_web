from django.db import models
from django.conf import settings

class Object(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, related_name='topics')

    def __str__(self):
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='subsections')

    def __str__(self):
        return self.name