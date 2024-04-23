from django.shortcuts import render,HttpResponse

# Create your views here.
def request_exception(request):
    a,b=5,0
    print(a," ",b)
    c = a/b
    return HttpResponse('Hello')
