from django.contrib import admin

# Register your models here.

from .models.product import Product
from .models.category import Category

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'category','description']








admin.site.register(Product,AdminProduct)
admin.site.register(Category)