from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def learnDjango(request):
    return HttpResponse('<h1>Learning Django</h1>')

def template_testing(request):
    context = {
        'name' : 'Mahesh',
        'city' : 'Himayatnagar',
        'company' : 'TCS',
        'hobby' : 'table-tennis',
        'date' : datetime.now(),
    }
    return render(request,'app1/index.html',context=context)

def if_for(request):
    context = {
        'name' : 'Mahesh',
        'digit' : 0,
    }
    return render(request,'app1/iffor.html',context=context)