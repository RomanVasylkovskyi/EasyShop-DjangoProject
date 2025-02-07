from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def main_page(request):
    return render(request, 'main_page.html')
