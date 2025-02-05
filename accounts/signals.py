"""
Create signals for the accounts app
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, Profile
from .service.mail_sender import send_activation_email


@receiver(post_save, sender=CustomUser)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
