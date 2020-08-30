from django.urls import path

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.view, name='view'),
    path('add/<int:pk>', basketapp.add, name='add'),
    path('remove/<int:pk>', basketapp.remove, name='remove'),
    path('move/', basketapp.move, name='move'),
]