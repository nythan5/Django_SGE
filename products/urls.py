from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    path('create/', views.ProductCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='delete'),

    path('api/v1/', views.ProductCreateListAPIView.as_view(), name='list-create-api'),
    path('api/v1/<int:pk>/',
         views.ProductRetrieveUpdateDestroyAPIView.as_view(), name='detail-api'),
]
