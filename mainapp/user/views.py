from django.conf.global_settings import ADMINS
from django.shortcuts import render, get_object_or_404, redirect
from .models import Admin
from .form import UserForm


def profile_page(request):
    return render(request, 'profile.html')

def store_page(request):
    return render(request, 'store.html')


def login_page(request):
    return render(request, 'login.html')

def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # Save the user to the database
            form.save() # Replace 'success_url_name' with your actual URL name
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})

def check_admin_login(request,login,password):
    if request.method == 'POST':
        admins = Admin.objects.all()
        for admin in admins:
            if admin.login == login and admin.password == password:
                return redirect('main')

