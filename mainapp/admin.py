from django.contrib import admin
from mainapp.models import Product, ProductCategory, Contact

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Contact)
