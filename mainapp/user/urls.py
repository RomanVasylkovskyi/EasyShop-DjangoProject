from django.urls import path
from . import views

urlpatterns = [
    path('checklogin/<int:pk>/',  views.check_admin_login , name='checklogin'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
]


