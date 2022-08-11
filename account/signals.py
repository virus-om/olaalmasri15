from django.db.models.signals import post_save
from django.contrib.auth.models import Account
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=Account)
def create_profile_pic(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Account)
def save_profile_pic(sender, instance, **kwargs):
    instance.profile.save()
