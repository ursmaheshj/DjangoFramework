from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('--------------in Home View-------------')
    return HttpResponse('Home Page: Middleware Demo')

def excep(request):
    print('--------------in Exception View-------------')
    result = 10/0
    return HttpResponse('Exception page')
