from django.db import models


# Create your models here.

# Категория продукта
class ProductCategory(models.Model):
    name = models.CharField(verbose_name='категория товара', max_length=100)
    desc = models.TextField(verbose_name='описание категории', blank=True)
    href = models.CharField(verbose_name='internal href', max_length=30, blank=False)

    def __str__(self):
        return f'{self.name} ({self.desc})'


# Продукты
class Product(models.Model):
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=100)
    desc = models.TextField(verbose_name='описание продукта', blank=True)
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=200, blank=True)
    img_src = models.ImageField(upload_to='products_img', blank=True)
    price = models.DecimalField(verbose_name='стоимость продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.IntegerField(verbose_name='количество единиц продукта', default=0)

    def __str__(self):
        return f'{self.name} ({self.desc}) за {self.price} руб., доступно {self.quantity} шт.'


# Контакты
class Contact(models.Model):
    location = models.CharField(verbose_name='город', max_length=200, unique=False, blank=False)
    phone = models.CharField(verbose_name='телефон', max_length=20)
    email = models.CharField(verbose_name='email', max_length=100)
    address = models.CharField(verbose_name='адрес', max_length=300)

    def __str__(self):
        return f'{self.location} ({self.address}) Телефон:{self.phone}; Email: {self.email}'
