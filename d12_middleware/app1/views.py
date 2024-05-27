from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    print('--------------in Home View-------------')
    return HttpResponse('Home Page: Middleware Demo')

def excep(request):
    print('--------------Before Excep View-------------')
    result = 10/0
    print('--------------After Excep View-------------')
    return HttpResponse('Exception page')

def profile(request):
    print('-----------inside profile view-----------')
    context = {
        'name':'Mahesh',
        'age':25,
    }
    return TemplateResponse(request,'app1/profile.html',context)
