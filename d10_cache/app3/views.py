from django.shortcuts import render

# Create your views here.
def fragmenthome(request):
    return render(request,'app3/home.html')