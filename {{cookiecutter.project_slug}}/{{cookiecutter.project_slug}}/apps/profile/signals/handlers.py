from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from ..models import Profile

@receiver(post_save, sender=get_user_model())
def user_handler(sender, instance, **kwargs):
    try:
        instance.profile
    except Profile.DoesNotExist:
        Profile.objects.create(user=instance)
