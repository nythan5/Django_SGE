from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView
from .models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs
