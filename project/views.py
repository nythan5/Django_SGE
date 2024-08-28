from django.shortcuts import render
from . import metrics
import json


def home(request):
    product_metrics = metrics.get_products_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        # Transformando um dicionario em JSON
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data)
    }

    return render(request, 'home.html', context)
