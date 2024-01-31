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

    try:
        wish_list = request.session.get('wish_list')
        pk_list = [i['id'] for i in wish_list]
        wish_list_products = []

        for product in Product.objects.all():
            if product.id in pk_list:
                wish_list_products.append(product)

    except Exception as ex:
        wish_list_products = []

    context = {
        'title': f'Список желаний {request.user.username}',
        'user': user,
        'wish_list': wish_list_products
    }

    return render(request, 'wish_list/user-wish-list.html', context)


def add_to_wish_list(request, pk):
    if request.method == 'POST':  # Проверяем запрос на метод POST
        if not request.session.get('wish_list'):  # Проверяем, есть ли в нашей сессии ключ wish_list
            request.session['wish_list'] = list()  # Если его нет, то создается пустой список
        else:  # Если он (ключ) есть, то мы создаем список с предыдущими значениями
            request.session['wish_list'] = list(request.session['wish_list'])

        # Проверяем, есть ли товар, который мы пытаемся добавить в нашем wish_list
        item_exists = next((i for i in request.session['wish_list'] if i['id'] == pk), False)

        # Принимаем данные нашего запроса
        app_data = {
            'id': pk
        }

        # Если товара, который мы пытаемся добавить в wish_list нет, то мы добавляем его
        if not item_exists:
            request.session['wish_list'].append(app_data)
            request.session.modified = True  # Указываем, что сессия была изменена
    return redirect(reverse('product:product_detail', kwargs={'slug': Product.objects.get(pk=pk).slug}))


def remove_from_wish_list(request, pk):
    if request.method == 'POST':
        for i in request.session['wish_list']:  # Пробегаемся по нашему списку из добавленный товаров
            if i['id'] == pk:  # Если находим этот товар, то удаляем его
                i.clear()

        # На месте удаленных товаров остается {}, поэтому их тоже нужно удалить
        while {} in request.session['wish_list']:
            request.session['wish_list'].remove({})

        # Тут мы проверяем, есть ли вообще у нас ключ wish_list в сессиях
        if not request.session['wish_list']:
            del request.session['wish_list']

        request.session.modified = True
    return redirect(reverse('product:product_detail', kwargs={'slug': Product.objects.get(pk=pk).slug}))


@login_required
def add_product_in_wish_list(request, slug):
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
