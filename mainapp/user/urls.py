from django.urls import path
from . import views

urlpatterns = [
    # path('checklogin/<int:pk>/',  views.check_admin_login , name='checklogin'),
    path('', views.profile_page, name='profile'),
    # path('login/', views.login_page, name='login'),
    # path('register/', views.register_user, name='register'),
]


