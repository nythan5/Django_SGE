from django.urls import path
from . import views

app_name = 'outflow'

urlpatterns = [
    path('list/', views.OutflowListView.as_view(), name='list'),
    path('create/', views.OutflowCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', views.OutflowDetailView.as_view(), name='detail'),
]
