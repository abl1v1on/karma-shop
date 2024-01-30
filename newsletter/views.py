from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from newsletter.models import Contact
from . import service


def create_new_contact_view(request):
    email = request.POST.get('user_email')
    if Contact.objects.filter(email=email).exists():
        raise ValidationError('Вы уже подписаны на рассылку')
    service.create_new_contact(email)
    return redirect('home')
