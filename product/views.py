from django.shortcuts import render
from django.views.generic import ListView, DetailView

from wish_list.models import WishList
from . import service
from .models import Product


def index(request):
    """Главная страница"""
    context = {
        'title': 'Главная страница',
        'latest_products': service.get_latest_products(),
        'sale_products': service.get_sale_products(),
    }
    return render(request, 'index.html', context)


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'single-product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title

        try:
            if self.request.session['wish_list']:
                pk_list = [i['id'] for i in self.request.session['wish_list']]
                context['is_in_wish_list'] = True if self.object.pk in pk_list else False
        except Exception as e:
            print(e)
            context['is_in_wish_list'] = False
        return context


class ProductCatalogView(ListView):
    model = Product
    ordering = '-id'
    context_object_name = 'products'
    template_name = 'category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Каталог'
        context['categories'] = service.get_all_categories()
        context['brands'] = service.get_all_brands()
        context['colors'] = service.get_all_colors()
        return context
