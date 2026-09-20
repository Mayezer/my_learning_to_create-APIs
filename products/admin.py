from django.contrib import admin
from products.models import Product

@admin.register(Product) # Adicionamos nossos campos de models.py na aba de Admin.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'description')
