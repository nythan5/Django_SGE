from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm
from project.metrics import get_sales_metrics
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from .serializers import OutflowSerializer


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 5
    permission_required = 'outflows.view_outflow'

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


class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    template_name = 'outflow_create.html'
    form_class = OutflowForm
    success_url = reverse_lazy('outflow:list')
    permission_required = 'outflows.add_outflow'


class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'


class OutflowCreateListAPIView(ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer


class OutflowRetrieveAPIView(RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
