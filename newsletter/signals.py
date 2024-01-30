from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Newsletter, Contact
from django.core.mail import send_mail
from .tasks import send_newsletter_task


@receiver(post_save, sender=Newsletter)
def send_newsletter(sender, instance, created, **kwargs):
    send_newsletter_task.delay()



