from django.shortcuts import render
from django_study.settings import BASE_DIR
import os
import json


header_menu = [
    {'href': 'main', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contact', 'name': 'контакты'},
]


# Главная страница
def main(request):
    products = [
        {'img_src': 'img/product-1.jpg',
         'header': 'Отличный стул',
         'desc': 'Расположитесь комфортно.'
        },
        {'img_src': 'img/product-2.jpg',
         'header': 'Стул повышенного качества',
         'desc': 'Не оторваться.'
        },
    ]

    context = {
        'title': 'магазин - главная',
        'header_menu': header_menu,
        'products': products,
    }

    return render(request, 'mainapp/index.html', context)


# Страница с продуктами
def products(request):
    product_menu = [
        {'href': 'pr_all', 'name': 'все'},
        {'href': 'pr_home', 'name': 'дом'},
        {'href': 'pr_office', 'name': 'офис'},
        {'href': 'pr_modern', 'name': 'модерн'},
        {'href': 'pr_classic', 'name': 'классика'},
    ]

    products = [
        {'img_src': 'img/product-11.jpg',
         'header': 'Стул повышенного качества',
         'desc': 'Не оторваться.'
        },
        {'img_src': 'img/product-21.jpg',
         'header': 'Стул повышенного качества',
         'desc': 'Не оторваться.'
        },
        {'img_src': 'img/product-31.jpg',
         'header': 'Стул повышенного качества',
         'desc': 'Не оторваться.'
        },
    ]

    context = {
        'title': 'магазин - продукты',
        'header_menu': header_menu,
        'product_menu': product_menu,
        'products': products,
    }

    return render(request, 'mainapp/products.html', context)


# Контакты
def contact(request):
    contacts = [
        #{'location': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        #{'location': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
        #{'location': 'Москва', 'phone': '+7-888-888-8888', 'email': 'info@geekshop.ru', 'address': 'В пределах МКАД'},
    ]

    with open(os.path.join(BASE_DIR, 'mainapp\json_data\contacts')) as f:
        data = f.read();

    contacts = json.loads(data)

    context = {
        'title': 'магазин - контакты',
        'header_menu': header_menu,
        'contacts': contacts,
    }

    return render(request, 'mainapp/contact.html', context)
