from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def main_page(request):
    return render(request, 'store/template/main_page.html')

def login_page(request):
    return render(request, 'store/template/login.html')

def register_page(request):
    return render(request, 'store/template/register.html')
