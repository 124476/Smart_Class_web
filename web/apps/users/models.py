import pathlib
import re
import sys
import uuid

import django.db.models
import django.contrib.auth.models
from django.conf import settings
import sorl.thumbnail


class LoginUserManager(django.contrib.auth.models.BaseUserManager):
    def normalize_email(self, email):
        email = super().normalize_email(email)
        email = email.lower()
        local_part, domain = email.split("@")

        local_part = local_part.split("+")[0]

        if domain in ["yandex.ru", "ya.ru"]:
            domain = "yandex.ru"
            local_part = local_part.replace(".", "-")
        elif domain == "gmail.com":
            local_part = local_part.replace(".", "")

        local_part = re.sub(r"\+.*", "", local_part)
        return f"{local_part}@{domain}"

    def get_queryset(self):
        return super().get_queryset().select_related("profile")

    def active(self):
        return self.get_queryset().filter(is_active=True)

    def by_mail(self, email):
        normalized_email = self.normalize_email(email)
        return self.get_queryset().filter(email=normalized_email).first()


class CustomUser(django.contrib.auth.models.AbstractUser):
    attempts_count = django.db.models.PositiveIntegerField(
        default=0,
    )

    def unlock_account(self):
        self.is_active = True
        self.attempts_count = 0
        self.save()

    class Meta:
        verbose_name = "кастомный пользователь"
        verbose_name_plural = "кастомные пользователи"

    def __str__(self):
        return self.username


class User(CustomUser):
    objects = LoginUserManager()

    def save(self, *args, **kwargs):
        self.email = User.objects.normalize_email(self.email)
        super().save(*args, **kwargs)

    class Meta:
        proxy = True

    def get_profile(self):
        return self.profile


if "makemigrations" not in sys.argv and "migrate" not in sys.argv:
    User._meta.get_field("email")._unique = True


class ProfileManager(django.db.models.Manager):
    def user_detail(self, pk):
        return (
            self.get_queryset()
            .filter(pk=pk)
            .values(
                "user__email",
                "user__first_name",
                "user__last_name",
                Profile.birthday.field.name,
                Profile.image.field.name,
                Profile.coffee_count.field.name,
            )
        )


class Profile(django.db.models.Model):
    def get_upload_file(self, filename):
        ext = filename.split(".")[-1]
        filename = f"{uuid.uuid4()}.{ext}"
        return pathlib.Path("users") / str(self.id) / filename

    objects = ProfileManager()

    user = django.db.models.OneToOneField(
        User,
        on_delete=django.db.models.CASCADE,
    )
    birthday = django.db.models.DateField(
        null=True,
        blank=True,
        help_text="Дата вашего рождения",
    )
    image = django.db.models.ImageField(
        verbose_name="изображение",
        upload_to=get_upload_file,
        blank=True,
        null=True,
        help_text="Аватарка",
    )
    is_main = django.db.models.BooleanField(
        verbose_name="Директор",
        default=False,
    )
    main_user = django.db.models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=django.db.models.CASCADE,
        related_name="main_user",
        verbose_name="Директор",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "дополнительное поле"
        verbose_name_plural = "дополнительные поля"
        ordering = ("user",)

    def __str__(self):
        return self.user.username

    def get_image_350x350(self):
        return sorl.thumbnail.get_thumbnail(
            self.image,
            "350x350",
            crop="center",
            quality=85,
        )