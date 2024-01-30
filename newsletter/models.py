from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email
