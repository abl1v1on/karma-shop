from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Brand, Category, Color, ProductImages


class ProductImageInline(admin.TabularInline):
    model = ProductImages


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_image', 'new_price', 'short_desc', 'brand', 'category')
    list_display_links = ('title', )
    search_fields = ('title', )
    search_help_text = 'Поиск по названию товара'
    inlines = [ProductImageInline]

    @admin.display(description='Изображение')
    def get_image(self, obj: Product):
        return mark_safe(f'<img src="/media/{obj.product_images.all()[0]}" width="140')
    #
    # @admin.display(description='Фото')
    # def get_product_pic(self, obj: Product):
    #     return mark_safe(f'<img src={obj.product_pic.url} width=140px> ')


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


@admin.register(ProductImages)
class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('product', 'get_image', )

    @admin.display(description='Изображение')
    def get_image(self, obj: ProductImages):
        return mark_safe(f'<img src="{obj.image.url}" width=150px"')