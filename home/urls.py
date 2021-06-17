from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/<item_id>/', views.add_one_to_bag, name='add_one_to_bag'),
    path('products/<product_id>', views.product, name='product'),
]
