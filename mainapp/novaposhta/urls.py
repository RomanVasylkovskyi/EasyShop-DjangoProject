from django.urls import path
from . import views

urlpatterns = [
    path('fetch-postomats/', views.fetch_postomats, name='fetch_postomats'),
]
