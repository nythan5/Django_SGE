from django.urls import path
from . import views

app_name = 'inflow'

urlpatterns = [
    path('list/', views.InflowListView.as_view(), name='list'),
    path('create/', views.InflowCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.InflowDetailView.as_view(), name='detail'),
]
