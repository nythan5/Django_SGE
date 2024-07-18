from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm
from project.metrics import get_sales_metrics


class OutflowListView(ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            qs = qs.filter(product__title__icontains=product)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = get_sales_metrics()
        return context


class OutflowCreateView(CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow:list')


class OutflowDetailView(DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
