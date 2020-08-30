from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from basketapp.models import Order, ORDER_START, OrderPosition
from mainapp.models import Product


# Create your views here.
@login_required
def view(request):
    order = Order.objects.filter(user=request.user, status=ORDER_START)
    if order.count():
        order = order.first()
        order_positions = OrderPosition.objects.filter(order=order)
    else:
        order_positions = []

    context = {
        'title': 'Корзина',
        'order': order,
        'order_positions': order_positions
    }

    return render(request, 'basketapp/basket.html', context)


@login_required
def add(request, pk):
    # Если попробовали добавить в корзину до авторизации, то было перенаправление
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    order = Order.objects.filter(user=request.user, status=ORDER_START)

    # Заказа еще не было
    if not order.count():
        order = Order(user=request.user)
        order.save()
        order_position = OrderPosition(order=order, product=product)
    # Пробуем найти позицию заказа ранее
    else:
        order = order.first()
        order_position = OrderPosition.objects.filter(order=order, product=product)
        # Была позиция
        if order_position.count():
            order_position = order_position.first()
        # Новая позиция
        else:
            order_position = OrderPosition(order=order, product=product)

    # Подводим итоги
    order_position.quantity += 1
    order_position.save()
    order.total += product.price
    order.save()

    order_positions = OrderPosition.objects.filter(order=order)

    context = {
        'title': 'Корзина',
        'order_positions': order_positions
    }

    if request.is_ajax():
        result = {
            'quantity': order_position.quantity,
            'total': order_position.quantity * order_position.product.price,
            'message': 'Товар успешно добавлен',
        }
        return JsonResponse({'result': result, 'total': order.total})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Убрать товар из заказа
@login_required
def remove(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_position = get_object_or_404(OrderPosition, product=product)
    order = get_object_or_404(Order, id=order_position.order.id, user=request.user)

    order_position.quantity -= 1
    order.total -= product.price
    order.save();

    if order_position.quantity:
        order_position.save()
    else:
        order_position.delete()

    if request.is_ajax():
        result = {
            'quantity': order_position.quantity,
            'total': order_position.quantity * order_position.product.price,
            'message': 'Товар успешно убран',
        }
        return JsonResponse({'result': result, 'total': order.total})
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Полностью убирает товарную позицию из заказа
@login_required
def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    order_position = get_object_or_404(OrderPosition, product=product)
    order = get_object_or_404(Order, id=order_position.order.id, user=request.user)

    order.total -= order_position.quantity * order_position.product.price
    order_position.delete()
    order.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

# Движение заявки по шагам
@login_required
def move(request):
    order = get_object_or_404(Order, user=request.user, status=ORDER_START)

    context = {
        'title': 'Корзина'
    }

    return render(request, 'basketapp/basket.html', context)
