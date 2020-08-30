from django.db import models
from django_study import settings
from mainapp.models import Product


# Create your models here.
ORDER_START = 'start'
ORDER_DELIVERY = 'delivery'
ORDER_CLOSED = 'closed'
ORDER_STATUSES = (
    (ORDER_START, 'Оформление'),
    (ORDER_DELIVERY, 'Доставка'),
    (ORDER_CLOSED, 'Закрыт'),
)


# Заказ
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    status = models.CharField(max_length=100, choices=ORDER_STATUSES, default=ORDER_START, verbose_name='Статус')
    total = models.PositiveIntegerField(default=0, verbose_name='Обшая стоимость')
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    update_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения')

    def __str__(self):
        return f'Заказ №{self.pk} пользователя {self.user.username} в статусе "{dict(ORDER_STATUSES)[self.status]}"'


# Позиция заказа
class OrderPosition(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Номер заказа')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Количество')

    def line_total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'Заказ №{self.order.pk} продукт "{self.product.name}" в количестве {self.quantity} шт.'
