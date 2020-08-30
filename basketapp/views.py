from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from basketapp.models import Order, ORDER_START, OrderPosition
from mainapp.models import Product


# Create your views here.
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


def add(request, pk):
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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Убрать товар из заказа
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

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# Движение заявки по шагам
def move(request):
    order = get_object_or_404(Order, user=request.user, status=ORDER_START)

    context = {
        'title': 'Корзина'
    }

    return render(request, 'basketapp/basket.html', context)
