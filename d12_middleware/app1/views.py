from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    print('--------------in View-------------')
    return HttpResponse('Middleware Demo')