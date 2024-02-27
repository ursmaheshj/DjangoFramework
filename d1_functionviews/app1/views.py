from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learnDjango(request):
    return HttpResponse('<h1>Learning Django</h1>')

def template_testing(request):
    
    context = {
        'name' : 'Mahesh',
        'city' : 'Himayatnagar',
        'company' : 'TCS',
    }
    return render(request,'app1/index.html',context=context)