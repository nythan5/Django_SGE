from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Inflow
from .forms import InflowForm
from django.contrib.auth.mixins import LoginRequiredMixin


class InflowListView(LoginRequiredMixin, ListView):
    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            qs = qs.filter(product__title__icontains=product)

        return qs


class InflowCreateView(LoginRequiredMixin, CreateView):
    model = Inflow
    template_name = 'inflow_create.html'
    form_class = InflowForm
    success_url = reverse_lazy('inflow:list')


class InflowDetailView(LoginRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
