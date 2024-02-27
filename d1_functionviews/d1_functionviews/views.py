from django.shortcuts import render
from datetime import datetime

def template_testing(request):
    context = {
        'name' : 'Mahesh',
        'city' : 'Himayatnagar',
        'company' : 'TCS',
        'hobby' : 'table-tennis',
        'date' : datetime.now(),
    }
    return render(request,'app1/index.html',context=context)