from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'app/login.html')

def register(request):
    return render(request, 'app/register.html')


def home(request):
    return render(request, 'app/home.html')

def logout(request):
    return render(request, 'app/logout.html')

def navbar(request):
    return render(request, 'navbar.html')


