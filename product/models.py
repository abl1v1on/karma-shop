from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    old_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Старая цена')
    new_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Новая цена')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 related_name='product_category', verbose_name='Категория')
    availibility = models.BooleanField(verbose_name='В наличии')
    short_desc = models.CharField(max_length=255, verbose_name='Короткое описание')
    long_desc = models.TextField(max_length=2000, verbose_name='Основное описание')
    width = models.IntegerField(blank=True, null=True, verbose_name='Ширина')
    height = models.IntegerField(blank=True, null=True, verbose_name='Длинна')
    depth = models.IntegerField(blank=True, null=True, verbose_name='Глубина')
    weight = models.FloatField(blank=True, null=True, verbose_name='Вес')
    freshness_duration = models.CharField(max_length=40, verbose_name='Продолжительность свежести')
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE,
                              related_name='product_brand', verbose_name='Бренд')
    slug = models.SlugField(max_length=70, unique=True, db_index=True, verbose_name='URL')
    is_sale = models.BooleanField(default=False)
    product_pic = models.ImageField(upload_to='product_pic/%Y', verbose_name='Изображение')
    color = models.ForeignKey('Color', on_delete=models.CASCADE,
                              related_name='product_color', verbose_name='Цвет')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    cat_name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.cat_name


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.brand_name


class Color(models.Model):
    color_name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.color_name
