from django.shortcuts import render, get_object_or_404
from django.urls import resolve
from mainapp.models import Product, ProductCategory, Contact


header_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


# Главная страница
def main(request):
    products = Product.objects.all().order_by('?')[:3]

    context = {
        'title': 'магазин - главная',
        'header_menu': header_menu,
        'products': products,
        'img_class': "img-product-270",
    }

    return render(request, 'mainapp/index.html', context)


# Страница с продуктами
def products(request, pk=None):
    # Формируем заголовок с категориями
    product_menu = [
        {'href': 'pr_all', 'name': 'все'},
    ]
    product_menu += ProductCategory.objects.all()

    # Получаем список продуктов для отображения
    current_url = resolve(request.path_info).url_name
    category = ProductCategory.objects.filter(href=current_url)

    if pk is not None:
        product = get_object_or_404(Product, pk=pk)
    else:
        product = None

    if category.count():
        if product is None:
            product = Product.objects.all().order_by('?').filter(category_id=getattr(category.first(), 'id'))[:1].first()
        products = Product.objects.exclude(pk=product.pk).order_by('?').filter(category_id=getattr(category.first(), 'id'))[:3]
    else:
        if product is None:
            product = Product.objects.all().order_by('?')[:1].first()
        products = Product.objects.exclude(pk=product.pk).order_by('?')[:3]

    context = {
        'title': 'магазин - продукты',
        'header_menu': header_menu,
        'product_menu': product_menu,
        'products': products,
        'product': product,
        'img_class': "img-product-370",
    }

    return render(request, 'mainapp/products.html', context)


# Контакты
def contact(request):
    contacts = Contact.objects.all()[:4]

    context = {
        'title': 'магазин - контакты',
        'header_menu': header_menu,
        'contacts': contacts,
    }

    return render(request, 'mainapp/contact.html', context)
