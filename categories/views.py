from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Category
from .forms import CategoryForm
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            qs = qs.filter(name__icontains=name)

        return qs


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category:list')


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category
    template_name = 'category_detail.html'


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    template_name = 'category_update.html'
    success_url = reverse_lazy('category:list')
    form_class = CategoryForm


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category:list')
