from django.core.mail import send_mail

from KarmaShop.celery import app
from .models import Contact, Newsletter


@app.task
def send_newsletter_task():
    last_newsletter_object = Newsletter.objects.all().last()
    for contact in Contact.objects.all():
        send_mail(
            f'{last_newsletter_object.subject}',
            f'{last_newsletter_object.text}',
            'djagnocelery@yandex.ru',
            [contact.email],
            fail_silently=False
        )


@app.task
def calc(a, b):
    return a + b
