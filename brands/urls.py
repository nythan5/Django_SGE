from django.urls import path
from . import views

app_name = 'brand'

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='list'),
    path('create/', views.BrandCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.BrandDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.BrandUpdateView.as_view(), name='update'),
]
