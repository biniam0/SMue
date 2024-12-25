from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')
