from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Coins, Upgrades

User = get_user_model()


@receiver(post_save, sender=User)
def create_related_model(sender, instance, created, **kwargs):
    if created:
        Coins.objects.create(user=instance)
        Upgrades.objects.create(user=instance)
