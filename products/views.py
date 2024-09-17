from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from categories.models import Category
from brands.models import Brand
from project import metrics
from django.contrib.auth.mixins import LoginRequiredMixin


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.GET.get('title')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        ns = self.request.GET.get('serie_number')

        if title:
            qs = qs.filter(title__icontains=title)

        if ns:
            qs = qs.filter(serie_number__icontains=ns)

        if category:
            qs = qs.filter(category__id=category)

        if brand:
            qs = qs.filter(brand__id=brand)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        context['product_metrics'] = metrics.get_products_metrics()
        return context


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    template_name = 'product_update.html'
    success_url = reverse_lazy('product:list')
    form_class = ProductForm


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product:list')
