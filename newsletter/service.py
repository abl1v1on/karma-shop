from newsletter.models import Contact
from django.core.mail import send_mail


def create_new_contact(user_email: str):
    Contact.objects.create(email=user_email)
    send_mail(
        'Вы подписались на рассылку!',
        'Бла бла бла',
        'djagnocelery@yandex.ru',
        [user_email],
        fail_silently=False
    )
