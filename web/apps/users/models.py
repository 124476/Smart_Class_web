from django.contrib.auth.models import AbstractUser
from django.db import models
from sorl.thumbnail import delete, get_thumbnail


class Role(models.Model):
    name = models.CharField("Название роли", max_length=100, unique=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    avatar = models.ImageField(
        "Аватар",
        upload_to="avatars/",
        null=True,
        blank=True,
    )
    roles = models.ManyToManyField(
        Role,
        related_name="users",
        blank=True,
        verbose_name="Роли",
    )
    is_created = models.BooleanField(
        verbose_name="Создатель",
        default=False,
    )

    main_user = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='subordinates',
        verbose_name="Главный пользователь"
    )

    def has_avatar(self):
        return self.avatar and self.avatar.url is not None

    def get_small_avatar(self):
        return get_thumbnail(self.avatar, "80", crop="center").url

    def get_large_avatar(self):
        return get_thumbnail(self.avatar, "200", crop="center").url

    def save(self, *args, **kwargs):
        try:
            old = User.objects.get(pk=self.pk)
            if old.has_avatar() and not self.has_avatar():
                delete(old.avatar)
        except User.DoesNotExist:
            pass
        super().save(*args, **kwargs)
