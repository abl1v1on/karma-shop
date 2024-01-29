from .models import Product, Category, Brand, Color


def get_all_products():
    return Product.objects.all()


def get_latest_products():
    return get_all_products().order_by('-id')[:9]


def get_sale_products():
    return Product.objects.filter(is_sale=True)[:5]


def get_all_categories():
    return Category.objects.all()


def get_all_brands():
    return Brand.objects.all()


def get_all_colors():
    return Color.objects.all()
