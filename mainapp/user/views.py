from django.conf.global_settings import ADMINS
from django.shortcuts import render, get_object_or_404, redirect
from .models import Admin


def login_page(request):
    return render(request, 'login.html')

def register_page(request):
    return render(request, 'register.html')

def check_admin_login(request,login,password):
    if request.method == 'POST':
        admins = Admin.objects.all()
        for admin in admins:
            if admin.login == login and admin.password == password:
                return redirect('main')





