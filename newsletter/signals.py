from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Newsletter, Contact
from django.core.mail import send_mail


@receiver(post_save, sender=Newsletter)
def send_newsletter(sender, instance, created, **kwargs):
    last_newsletter_index = len(Newsletter.objects.all())
    last_newsletter_object = Newsletter.objects.get(pk=last_newsletter_index)
    for contact in Contact.objects.all():
        send_mail(
            f'{last_newsletter_object.subject}',
            f'{last_newsletter_object.text}',
            'djagnocelery@yandex.ru',
            [contact.email],
            fail_silently=False
        )
