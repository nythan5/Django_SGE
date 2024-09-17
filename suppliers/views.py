from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Supplier
from .forms import SupplierForm
from django.contrib.auth.mixins import LoginRequiredMixin


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs


class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Supplier
    template_name = 'supplier_create.html'
    form_class = SupplierForm
    success_url = reverse_lazy('supplier:list')


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'


class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Supplier
    template_name = 'supplier_update.html'
    success_url = reverse_lazy('supplier:list')
    form_class = SupplierForm


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Supplier
    template_name = 'supplier_delete.html'
    success_url = reverse_lazy('supplier:list')
