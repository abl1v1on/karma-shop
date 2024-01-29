from django.contrib.auth import get_user_model
from django.db import models

from product.models import Product


class WishList(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                             related_name='user_wish_list', verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='product_wish_list', verbose_name='Товар')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')

    class Meta:
        verbose_name = 'Список желаемого'
        verbose_name_plural = 'Списки желаемого'

    def __str__(self):
        return self.user.username
