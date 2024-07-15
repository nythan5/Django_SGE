from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.BrandListView.as_view(), name='brand_list')
]
