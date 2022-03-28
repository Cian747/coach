from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'landing.html')

def register(request):
    return render(request,'registration/register.html')

def login(request):
    return render(request,'registration/login.html')
