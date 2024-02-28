from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'app1/home.html')

def index(request):
    return render(request,'app1/index.html')

def about(request):
    return render(request,'app1/about.html')

def base(request):
    return render(request,'app1/base.html')