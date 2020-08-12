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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django_study import settings
from mainapp import views as mainapp

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('authapp.urls', namespace='auth')),

    path('', mainapp.main, name='main'),

    path('products/',               mainapp.products, name='products'),
    path('products/pr_all/',        mainapp.products, name='pr_all'),
    path('products/pr_chair/',      mainapp.products, name='pr_chair'),
    path('products/pr_armchair/',   mainapp.products, name='pr_armchair'),
    path('products/pr_divan/',      mainapp.products, name='pr_divan'),

    path('contact/', mainapp.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
