from basketapp.models import Order, OrderPosition, ORDER_START
from django import template
register = template.Library()


# Функция для получения количества позиций в корзине
@register.simple_tag
def get_basket_count(request):
    count = 0

    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, status=ORDER_START)
        if order.count():
            count = OrderPosition.objects.filter(order=order.first()).count()
    return count


# Функция для получения стоимости текущей корзины в статусе "Оформление"
@register.simple_tag
def get_basket_price(request):
    price = ''

    if request.user.is_authenticated:
        order = Order.objects.filter(user=request.user, status=ORDER_START)
        if order.count():
            price = order.first().total
    if price > 0:
        # Используем неразрывный пробел, чтобы отобразилось в одну строку
        price = f'{price}\xa0руб.'
    return price
