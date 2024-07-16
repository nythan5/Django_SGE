from django.urls import path
from . import views

app_name = 'brand'

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='list'),
    path('create/', views.BrandCreateView.as_view(), name='create')
]
