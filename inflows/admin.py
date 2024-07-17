from django.contrib import admin
from .models import Inflow

# Register your models here.


class InflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'quantity', 'created_at')
    search_fields = ('product__title', 'supplier__name')


admin.site.register(Inflow, InflowAdmin)
