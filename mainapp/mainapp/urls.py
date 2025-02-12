from django.contrib import admin
from django.urls import path
import store.views as store_views

urlpatterns = [

    path('', store_views.main_page, name='start'),
    path('admin/', admin.site.urls, name='admin'),
    path('main/', store_views.main_page, name='main'),
]
