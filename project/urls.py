from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render


urlpatterns = [
    path('admin/', admin.site.urls),
    path('brands/', include('brands.urls')),


]
