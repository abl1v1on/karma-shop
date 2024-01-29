from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Brand, Category, Color


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_product_pic', 'new_price', 'short_desc', 'brand', 'category')
    list_display_links = ('title', 'get_product_pic')

    @admin.display(description='Фото')
    def get_product_pic(self, obj: Product):
        return mark_safe(f'<img src={obj.product_pic.url} width=140px> ')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name', 'slug')
    list_display_links = ('brand_name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name', 'slug')
    list_display_links = ('cat_name', )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name', 'slug')
    list_display_links = ('color_name', )
