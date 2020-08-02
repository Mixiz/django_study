"""django_study URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainapp import views as mainapp

urlpatterns = [
    #path('admin/', admin.site.urls),

    path('', mainapp.main, name='main'),

    path('products/',            mainapp.products, name='products'),
    path('products/pr_all/',     mainapp.products, name='pr_all'),
    path('products/pr_home/',    mainapp.products, name='pr_home'),
    path('products/pr_office/',  mainapp.products, name='pr_office'),
    path('products/pr_modern/',  mainapp.products, name='pr_modern'),
    path('products/pr_classic/', mainapp.products, name='pr_classic'),

    path('contact/', mainapp.contact, name='contact'),
]
