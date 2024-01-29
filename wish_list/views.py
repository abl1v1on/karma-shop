from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from product.models import Product
from . import service


def show_user_wish_list(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    if request.user.id != user.id:
        return redirect('home')

    context = {
        'title': f'Список желаний {request.user.username}',
        'user': user
    }

    return render(request, 'wish_list/user-wish-list.html', context)


@login_required
def add_product_in_wish_List(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if service.check_item(request.user.id, product.id):
        return redirect('home')
    service.add_item_in_wish_list(request.user.id, product.id)
    return redirect(reverse('product:product_detail', kwargs={'slug': product.slug}))


@login_required
def remove_product_from_wish_list(request, slug):
    product = get_object_or_404(Product, slug=slug)

    if not service.check_item(request.user.id, product.id):
        return redirect('home')
    service.remove_item_from_wish_list(request.user.id, product.id)
    return redirect(reverse('product:product_detail', kwargs={'slug': product.slug}))