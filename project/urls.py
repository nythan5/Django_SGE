from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', include('brands.urls')),
    path('categories/', include('categories.urls')),
    path('suppliers/', include('suppliers.urls')),
    path('inflows/', include('inflows.urls')),
    path('outflows/', include('outflows.urls')),
    path('products/', include('products.urls')),
    path('home/', views.home, name='home'),


    path('login/', LoginView.as_view(), name="login")


]
