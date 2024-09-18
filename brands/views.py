from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 5
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs


class BrandCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand:list')
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brand:list')
    form_class = BrandForm
    permission_required = 'brands.update_brand'


class BrandDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand:list')
    permission_required = 'brands.delete_brand'
