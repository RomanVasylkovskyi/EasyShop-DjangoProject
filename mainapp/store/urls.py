from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.create_product, name='product_create'),
    path('store/create/', views.create_product, name='create_product'),
    path('store/products/', views.product_list, name='product_list'), 
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
]
