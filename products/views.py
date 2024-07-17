from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from categories.models import Category
from brands.models import Brand


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            qs = qs.filter(name__icontains=title)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()
        return context


class ProductCreateView(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('product:list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    success_url = reverse_lazy('product:list')
    form_class = ProductForm


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product:list')
