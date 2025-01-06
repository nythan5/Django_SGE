from django.shortcuts import render
from . import metrics
import json
from django.contrib.auth.decorators import login_required
from ai.models import AIResult


@login_required(login_url='login')
def home(request):
    product_metrics = metrics.get_products_metrics()
    sales_metrics = metrics.get_sales_metrics()
    daily_sales_data = metrics.get_daily_sales_data()
    daily_sales_quantity_data = metrics.get_daily_sales_quantity_data()
    graphic_product_category_metric = metrics.get_graphic_product_category_metric()
    graphic_product_brand_metric = metrics.get_graphic_product_brand_metric()
    ai_result = AIResult.objects.first()

    context = {
        'product_metrics': product_metrics,
        'sales_metrics': sales_metrics,
        # Transformando um dicionario em JSON
        'daily_sales_data': json.dumps(daily_sales_data),
        'daily_sales_quantity_data': json.dumps(daily_sales_quantity_data),
        'product_count_by_category': json.dumps(graphic_product_category_metric),
        'product_count_by_brand': json.dumps(graphic_product_brand_metric),
        'ai_result': ai_result
    }

    return render(request, 'home.html', context)
