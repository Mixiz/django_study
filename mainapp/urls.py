from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('',                        mainapp.products, name='products'),
    path('<int:pk>',                mainapp.products, name='products'),
    path('pr_all/',                 mainapp.products, name='pr_all'),
    path('pr_all/<int:pk>',         mainapp.products, name='pr_all'),
    path('pr_chair/',               mainapp.products, name='pr_chair'),
    path('pr_chair/<int:pk>',       mainapp.products, name='pr_chair'),
    path('pr_armchair/',            mainapp.products, name='pr_armchair'),
    path('pr_armchair/<int:pk>',    mainapp.products, name='pr_armchair'),
    path('pr_divan/',               mainapp.products, name='pr_divan'),
    path('pr_divan/<int:pk>',       mainapp.products, name='pr_divan'),
]