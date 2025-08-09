from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=255)
    object = models.ForeignKey(Object, on_delete=models.CASCADE,
                               related_name='topics')

    def __str__(self):
        return self.name


class Subsection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE,
        related_name='subsections',
    )
    image = models.ImageField(
        upload_to='subsection_images/',
        blank=True,
        null=True,
        verbose_name='Изображение',
    )

    def __str__(self):
        return self.name
