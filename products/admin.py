from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'brand',
                    'serie_number', 'quantity', 'created_at')
    search_fields = ('title', 'brand__name', 'category__name')


admin.site.register(Product, ProductAdmin)
