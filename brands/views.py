from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BrandListView(LoginRequiredMixin, ListView):
    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs


class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    template_name = 'brand_create.html'
    form_class = BrandForm
    success_url = reverse_lazy('brand:list')


class BrandDetailView(DetailView):
    model = Brand
    template_name = 'brand_detail.html'


class BrandUpdateView(LoginRequiredMixin, UpdateView):
    model = Brand
    template_name = 'brand_update.html'
    success_url = reverse_lazy('brand:list')
    form_class = BrandForm


class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brand:list')
