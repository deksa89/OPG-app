from django.contrib import admin
from .models import Product, Farm

# Register your models here.
admin.site.register(Farm)
admin.site.register(Product)