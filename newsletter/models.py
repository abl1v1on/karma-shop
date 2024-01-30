from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=100, verbose_name='Почта')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(max_length=4000, verbose_name='Текст рассылки')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return self.subject
