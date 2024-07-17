from django.urls import path
from . import views

app_name = 'category'

urlpatterns = [
    path('list/', views.CategoryListView.as_view(), name='list'),
    path('create/', views.CategoryCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.CategoryDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.CategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='delete'),
]
