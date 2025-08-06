from django.db.models.signals import post_save
from django.dispatch import receiver

import apps.users.models


@receiver(post_save, sender=apps.users.models.CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        apps.users.models.Profile.objects.create(user=instance)


__all__ = ()