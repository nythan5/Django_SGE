from django.urls import path
from . import views

app_name = 'supplier'

urlpatterns = [
    path('list/', views.SupplierListView.as_view(), name='list'),
    path('create/', views.SupplierCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.SupplierDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.SupplierUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='delete'),

    path('api/v1/', views.SupplierCreateListAPIView.as_view(),
         name='list-create-api'),
    path('api/v1/<int:pk>/',
         views.SupplierRetrieveUpdateDestroyAPIView.as_view(), name='detail-api'),
]
