from django.urls import path
from . import views

app_name = 'brand'

urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='list'),
    path('create/', views.BrandCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.BrandDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.BrandUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BrandDeleteView.as_view(), name='delete'),

    path('api/v1/', views.BrandCreateListAPIView.as_view(), name='list-create-api'),
    path('api/v1/<int:pk>/',
         views.BrandRetrieveUpdateDestroyAPIView.as_view(), name='detail-api'),

]
